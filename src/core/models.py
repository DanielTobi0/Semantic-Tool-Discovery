from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ToolChunk:
    tool_name: str
    server: str
    purpose: str
    capabilities: str
    parameters: str

    @property
    def text(self) -> str:
        return (
            f"Tool: {self.tool_name}\n"
            f"Purpose: {self.purpose}\n"
            f"Capabilities: {self.capabilities}\n"
            f"Parameters: {self.parameters}"
        )


@dataclass(slots=True)
class RetrievedChunk:
    tool_name: str
    server: str
    text: str
    score: float | None
    distance: float | None
