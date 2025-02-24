# Python – Words Frequency in String Shorthands

####################### METHOD 1 ################################

def freq(input):
    a= input.split()
    b= set(a)
    d= {}
    # print(b)
    for i in range(0,len(a)):
        count1=0
        for j in range(0,len(a)):
            if (a[i]==a[j]):
                count1+=1
        d[a[i]]=count1
    print(d)


# input= "My name is subhanshu jain name jain is subhanshu jain"
input= "aaa bbb aaa ccc ccc ccc ccc cccc bb bbb bbb aa aaa aaaa aaa"
freq(input)



################### METHOD2 ###############################




# Python3 code to demonstrate working of
# Words Frequency in String Shorthands
# Using dictionary comprehension + count() + split()
 
# Initializing string
test_str = 'My name is subhanshu jain name jain is subhanshu jain'
 
# Words Frequency in String Shorthands
# Using dictionary comprehension + count() + split()
res = {key: test_str.count(key) for key in test_str.split()}
 
# Printing result
print("The words frequency : " + str(res))



##################### Testing ###############################

freq1= "aaa bbb aaa ccc ccc ccc ccc cccc bb bbb bbb aa aaa aaaa aaa"

d1={key: freq1.count(key) for key in freq1.split()}

print(d1)