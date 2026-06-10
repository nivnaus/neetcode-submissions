class Solution:


    def encode(self, strs: List[str]) -> str:
        # If the list is completely empty, return a unique flag string
        if not strs:
            return "EMPTY_LIST"
        return '¶'.join(strs)

    def decode(self, s: str) -> List[str]:
        # If we see our unique flag, return a true empty list
        if s == "EMPTY_LIST":
            return []
        return s.split('¶')