from __future__ import annotations

import ast
from pathlib import Path
from typing import Any

from src.core.models import ToolChunk


def _safe_extract_str(dct: dict[str, Any], key: str) -> str:
    value = dct.get(key, "")
    return value if isinstance(value, str) else str(value)


def parse_tools_file(tools_file: str | Path) -> list[ToolChunk]:
    path = Path(tools_file)
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source)

    chunks: list[ToolChunk] = []

    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
            continue

        var_name = node.targets[0].id
        if not var_name.endswith("_mcp_tools"):
            continue

        server_name = var_name.removesuffix("_mcp_tools")
        try:
            tools_dict = ast.literal_eval(node.value)
        except Exception as exc:  # pragma: no cover
            raise ValueError(f"Unable to parse tools from {var_name}") from exc

        if not isinstance(tools_dict, dict):
            continue

        for tool_key, tool_spec in tools_dict.items():
            if not isinstance(tool_key, str) or not isinstance(tool_spec, dict):
                continue

            chunks.append(
                ToolChunk(
                    tool_name=_safe_extract_str(tool_spec, "Tool") or tool_key,
                    server=server_name,
                    purpose=_safe_extract_str(tool_spec, "Purpose"),
                    capabilities=_safe_extract_str(tool_spec, "Capabilities"),
                    parameters=_safe_extract_str(tool_spec, "Parameters"),
                )
            )

    return chunks
