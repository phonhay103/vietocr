import pandas as pd
from collections import Counter

def create_df(err_file_path):
    words = []
    with open(err_file_path) as f:
        lines = f.read().splitlines()

        for line in lines:
            _, gt_word, _, _, pred_word = line.split()
            words.append((gt_word, pred_word))

    word_counter = Counter(words)

    df = pd.DataFrame.from_dict(word_counter, orient='index', columns=['Count'])
    df[['gt_word', 'pred_word']] = pd.DataFrame(df.index.tolist(), index=df.index)
    df = df.sort_values('Count', ascending=False)
    df = df.reset_index(drop=True)
    df = df[['gt_word', 'pred_word', 'Count']]
    return df

old_df = create_df('word_errors_new.txt')
# old_df.to_csv('word_errors_new.csv')

# new_df = create_df('word_errors.txt')
# new_df.to_csv('word_errors.csv')

print(len(set(old_df[old_df.Count >= 5].gt_word.values)))
print(len(set(old_df[old_df.Count >= 4].gt_word.values)))
print(len(set(old_df[old_df.Count >= 3].gt_word.values)))
print(len(set(old_df[old_df.Count >= 2].gt_word.values)))
