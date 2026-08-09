class Solution:

    def encode(self, strs: List[str]) -> str:
        words = []
        for s in strs:
            size = len(s)
            words.append(f"{size}#{s}")
            # print(s)
        return ''.join(words)

    def decode(self, s: str) -> List[str]:
        message = []
        pointer = 0
        for index, c in enumerate(s):
            if pointer < index and s[index] == '#':
                count = int(s[pointer:index])
                # print("COUNT", count)
                message.append(s[index+1:index+count+1])
                # print("MESSAGE", message)
                pointer = index+count+1

        return message
