result = "1"
        for i in range(2, n + 1):
            result = self.RLE(result)
        return result

    def RLE(self, s: str) -> str:
        count = 1
        result = []
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result.append(str(count) + s[i - 1])
                count = 1
        result.append(str(count) + s[-1])
        return "".join(result)
