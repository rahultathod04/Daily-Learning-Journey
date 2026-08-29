class Solution(object):
    def majorityFrequencyGroup(self, s):
        counts = Counter(s)
        
        # Step 2: Group characters by their frequency value
        freq_groups = {}
        for char, freq in counts.items():
            if freq not in freq_groups:
                freq_groups[freq] = []
            freq_groups[freq].append(char)
            
        best_k = -1
        best_size = -1
        
        # Step 3: Find the winning frequency group
        for k, chars in freq_groups.items():
            current_size = len(chars)
            
            # Primary check: largest group size
            if current_size > best_size:
                best_size = current_size
                best_k = k
            # Secondary check: higher frequency tie-breaker
            elif current_size == best_size:
                if k > best_k:
                    best_k = k
                    
        # Step 4: Combine the characters into the output string
        return "".join(freq_groups[best_k])
        