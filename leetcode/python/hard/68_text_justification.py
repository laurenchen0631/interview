from math import ceil


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> List[str]:
        res = []
        cur_line = []
        cur_count = 0
        i = 0
        while i < len(words):
            word = words[i]
            cur_line.append(word)
            cur_count += len(word)
            if cur_count + (len(cur_line) - 1) <= maxWidth:
                i += 1
                continue
            
            # remove new added and
            cur_line.pop()
            cur_count -= len(word)

            #  make a new line
            gap = max(1, len(cur_line) - 1)
            spaces = maxWidth - cur_count
            line = []
            for w in cur_line:
                line.append(w)
                used = ceil(spaces / gap) if gap else 0
                if spaces >= used:
                    line.append(" " * used)
                else:
                    line.append(" " * spaces)
                spaces -= used
                gap -= 1
            res.append(''.join(line))
            cur_line = []
            cur_count = 0
        
        # special case: last line is left-justified
        if cur_line:
            trailing = " " * (maxWidth - cur_count - len(cur_line) + 1)
            res.append(" ".join(cur_line) + trailing)
        
        return res

