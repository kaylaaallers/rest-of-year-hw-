names = ["Gen", "Kayla", "Justis", "Leo", "Maikel", "Tianhao", "Annie", "Steph","owen","Mikki"]
def words_5(words):
    count = 0
    for i in words:
        if len(i) == 5:
            count += 1
        return count

def sum_to_even(nlist):
    """Sumn all the elements in a list up to but not including the first even number"""
    sum = 0
    for i in nlist:
        if i % 2 == 0:
            break
        else:
            sum+=i
        return sum

