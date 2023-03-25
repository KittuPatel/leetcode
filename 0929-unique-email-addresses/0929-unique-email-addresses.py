class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashset = set()
        
        for email in emails:
            temp = email.split('@')
            
            first = temp[0]
            second = temp[1]
            
            first = first.replace('.', '')
            
            local = first.split('+')
            new = local[0] + '@' + second
            print(new)
            hashset.add(new)
            
            
        return len(hashset)
            
            
            