class Solution:

    def encode(self, strs: List[str]) -> str:
        string = "$".join(strs)
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        strings = s.split("$")
        print(strings)
        return strings
