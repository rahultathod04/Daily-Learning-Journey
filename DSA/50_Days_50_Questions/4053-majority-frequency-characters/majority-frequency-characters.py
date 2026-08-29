class Solution(object):
    def majorityFrequencyGroup(self, s):
        counts = Counter(s)
        freq_groups = {}
        for char, freq in counts.items():
            if freq not in freq_groups:
                freq_groups[freq] = []
            freq_groups[freq].append(char)
            
        best_k = -1
        best_size = -1
        
        for k, chars in freq_groups.items():
            current_size = len(chars)
            
            if current_size > best_size:
                best_size = current_size
                best_k = k

            elif current_size == best_size:
                if k > best_k:
                    best_k = k
                    
        return "".join(freq_groups[best_k])
        