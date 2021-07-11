class CutWords:
    """xiaoli分词是一个主要用于某个领域的词汇，可以自行添加词库，删除词库"""
    def __init__(self):
        self.data = self.get_data()
        self.cut_word_list_ = []

    def get_data(self):
        with open("D:/download/windows/qinhua_word_dict/THUOCL_it.txt", "r", encoding="utf8") as f:
            data = {line.split("\t")[0].strip(): 1 for line in f.readlines() if line}
        return data

    def cut(self, sentence, max_length=4):
        """前向最大匹配"""
        i = 0
        while i < len(sentence):
            temp = sentence[i:i + 4]
            if temp in self.data:
                self.cut_word_list_.append(temp)
                i += 4
            elif temp[:-1] in self.data:
                self.cut_word_list_.append(temp[:-1])
                i += 3
            elif temp[:-2] in self.data:
                self.cut_word_list_.append(temp[:-2])
                i += 2
            else:
                self.cut_word_list_.append(temp[0])
                i += 1
        return self.cut_word_list_

    def add_word(self, word):
        self.data[word] = 1

    def stop_word(self, stop_list):
        for word in stop_list:
            if word and (word in self.cut_word_list_):
                self.cut_word_list_.remove(word)
        return self.cut_word_list_

    def __repr__(self):
        return "CutWords：xiaoli分词是一个主要用于某个领域的词汇，可以自行添加词库，删除词库"\
