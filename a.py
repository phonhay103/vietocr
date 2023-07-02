import pandas as pd

def create_word_df(words):
    words_count = {}
    for item in words:
        key = (item.split()[1], item.split()[-1])
        if key in words_count:
            words_count[key] += 1
        else:
            words_count[key] = 1

    words_count = [(k[0], k[1], v) for k, v in words_count.items()]
    words_count = sorted(words_count, key=lambda x: x[2], reverse=True)
    columns = ['label', 'prediction', 'times']
    return pd.DataFrame(words_count, columns=columns)

####################################################
# Kiểm tra lại các từ đã gen
####################################################

with open('word_errors_new.txt', 'r') as f:
    words = f.readlines()

with open('word_errors.txt', 'r') as f:
    words2 = f.readlines()

with open('CGGANv2.2_generated.txt') as f:
    generated_words = f.read().splitlines()

df_old = create_word_df(words)
df = create_word_df(words2)
df['old_times'] = df_old.times
df = df[df.times > 2]
df = df[df.times >= df.old_times]
df = df[df.label.isin(generated_words)]
all_words = set(df.label.values)

with open('CGGANv2.2_need_check.txt', 'w') as f:
    f.write('\n'.join(all_words).rstrip())

#####################################################
# Thêm các từ mới để gen
####################################################

with open('word_errors.txt', 'r') as f:
    words = f.readlines()

with open('CGGANv2.2_generated.txt') as f:
    generated_words = f.read().splitlines()

df = create_word_df(words)
df = df[df.times > 2]
df = df[~df['label'].str.contains('-')]
df = df[~df.label.isin(generated_words)]
all_words = set(df.label.values)

with open('CGGANv2.2_new_gen.txt', 'w') as f:
    f.write('\n'.join(all_words).rstrip())