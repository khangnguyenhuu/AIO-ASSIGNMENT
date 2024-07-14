import pandas as pd
df = pd.read_csv("advertising.csv")

data = df.to_numpy()

# cau 15: Lay gia tri lon nhat va chi muc tuong ung cua no tren cot Sales:
maxSales = df['Sales'].max()
index_maxSales = df['Sales'].idxmax()
print("Dap an cau 15 la: Max: {} - Index: {}".format(maxSales, index_maxSales))
# dap an c

# cau 16: Gia tri trung binh cua cot TV la:
mean_value_TV = df['TV'].mean()
print("Dap an cau 16 la:", round(mean_value_TV))
# dap an b

# cau 17: So luong ban ghi co gia tri tai cot Sales lon hon hoac bang 20 la:
count_of_Sales_20 = len(df[df['Sales'] >= 20])
print("Dap an cau 17 la:", count_of_Sales_20)
# dap an a

# cau 18: Tinh gia tri trung binh cua cot Radio thoa man dieu kien gia tri tuong ung tren cot Sales lon hon hoac bang 15:
mean_value_Radio_Sales_15 = df.loc[df["Sales"] >= 15, 'Radio'].mean()
print("Dap an cau 18 la:", round(mean_value_Radio_Sales_15, 1))
# dap an b

# cau 19: Tinh tong cac hang cua cot Sales voi dieu kien gia tri Newspaper lon hon gia tri trung binh cua cot Newspaper:
sum_Sales_Newspaper = df.loc[df['Newspaper']
                             >= df['Newspaper'].mean(), 'Sales'].sum()
print("Dap an cau 19 la:", sum_Sales_Newspaper)
# dap an c

# cau 20: Goi gia tri trung binh cua cot Sales la A. Tao ra mang moi scores chua cac gia tri Good, Average va Bad sao cho: neu gia tri hien
# tai > A => gia tri trong mang moi la Good, <A thi se la Bad va =A la Average. Sau do in ra ket qua scores[7:10]

scores = []
A = df['Sales'].mean()
for i in df['Sales']:
    if i > A:
        scores.append('Good')
    elif i < A:
        scores.append('Bad')
    else:
        scores.append('Average')

print("Dap an cau 20 la:", scores[7:10])
# dap an c

# cau 21: Goi gia tri tren cot Sales gan nhat voi gia tri trung binh cung chinh cot Sales la A. Tao ra mang moi scores chua cac gia tri Good, Average
# va Bad sao cho: neu gia tri hien tai > A => gia tri trong mang moi la Good, <A thi se la Bad va =A la Average. Sau do in ra ket qua scores[7:10]

scores_2 = []
closest_A = df['Sales'].iloc[(df['Sales']-A).abs().argsort()[0]]
for i in df['Sales']:
    if i > closest_A:
        scores_2.append('Good')
    elif i < closest_A:
        scores_2.append('Bad')
    else:
        scores_2.append('Average')

print("Dap an cau 21 la:", scores_2[7:10])
# dap an c
