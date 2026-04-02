class Solution:
    def encoder_coder(self, enc:str):
        return enc[::-1]

    def encode(self, strs: List[str]) -> str:
        if strs ==[]:
            return str(None)
        
        if strs==[""]:
            return ""

        encoded_strs =[]
        for i in range(len(strs)):
            encoded_strs.append(self.encoder_coder(strs[i]))
        return ";".join(encoded_strs)

    def decode(self, s: str) -> List[str]:
        if s=='':
            return [""]
        
        if s==str(None):
            return []
        
        decoded_str = [i[::-1] for i in s.split(';')]
        print(decoded_str)
        return decoded_str
