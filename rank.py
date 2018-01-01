
import re

# File Upload
f = open("C:/Users/neeraj/Desktop/mtech/cvs/12.txt", "r")
file1=f.read()
f.close()
str(file1)

start = file1.find('DOMAIN/PROFESSIONAL EXPERIENCE') 
end = file1.find('EDUCATIONAL CREDENTIALS')
str(file1[start:end])

new=re.findall(r".(\d{1,2}).\D",file1[start:end])
print("experience in each company: ",new)
new_list=[]
for each_obj in new:
    obj=int(each_obj)
    new_list.append(obj)

add=sum(new_list) 
    
resume_count=0
resume_rank=0

if add==0:
    resume_count=0
    resume_rank=0
    print("resume count for exp",resume_count)
   # print("resume rank is",resume_rank)

elif add <5:
    resume_count=resume_count+2
    resume_rank=resume_rank+2
    print("resume count for exp",resume_count)
    #print("resume rank is",resume_rank)
    
elif add >=5:
    resume_count=resume_count+4
    resume_rank=resume_rank+4
    print("resume count for exp",resume_count)
    #print("resume rank is",resume_rank)
    
else:
    pass
    
print()
    
    
new2=re.findall(r"(\d{1,2}).\W\D", file1[start:end]) 
print("no of companies :",len(new2))
data1=len(new2)
#resume_count=0

if data1==0:

    resume_count=0
    resume_rank=0
    print("resume count for no_of_comp",resume_count)
    #print("resume rank is",resume_rank)

elif data1 <5:

    resume_count=resume_count+3
    resume_rank=resume_rank+3
    print("resume count for no_of_comp ",resume_count)
    #print("resume rank is",resume_rank)
    
elif data1 >=5:

    resume_count=resume_count+6
    resume_rank=resume_rank+6       
    print("resume count for no_of_comp ",resume_count)
    #print("resume rank is",resume_rank)
    
else:
    pass
    
print()
    

start2 = file1.find('Certifications') 
end2 = file1.find('DOMAIN KNOWLEDGE IN  INDUSTRY')
str(file1[start2:end2])
    
new4=re.findall(r"(\d{1,2}).\W\D", file1[start2:end2]) 
print("certificates: ",len(new4))
data2=len(new4)

#resume_count=0
if data2==0:

    resume_count=0
    resume_rank=0
    print("resume count for certificates",resume_count)
    #print("resume rank is",resume_rank)

elif data2 <5:
    resume_count=resume_count+1
    resume_rank=resume_rank+1
    print("resume count for certificates",resume_count)
    #print("resume rank is",resume_rank)
elif data2 >=5:
    
    resume_count=resume_count+2
    resume_rank=resume_rank+2
    print("resume count for certificates",resume_count)
    #print("resume rank is",resume_rank)
else:
    pass

print()

start1 = file1.find('EDUCATIONAL CREDENTIALS') 
end1 = file1.find('ACADEMIC ACHIEVEMENTS & ACTIVITIES')
x=str(file1[start1:end1])


numbers = []
rx = r'[-\d.]+\d%'

    # loop over the results
for match in re.finditer(rx, x):
    interval = match.group(0).split('-')
    for number in interval:
        if 0 <= float(number.strip('%')) <= 100:
            numbers.append(number)

numbers[:] = [s.strip("%") for s in numbers]
print("percentages are and max is",max(numbers),numbers)
mymax=max(numbers)
maxim=int(mymax)


if maxim <50:
    resume_count=resume_count+1
    resume_rank=resume_rank+1
    print("resume count for GPA",resume_count)
    print("resume rank is",resume_rank)
    
elif maxim >=50:

    resume_count=resume_count+2
    resume_rank=resume_rank+2
    print("resume count for GPA",resume_count)
    print("resume rank is",resume_rank)
   
else:
    pass

print()

nod=re.findall(r"\D(\d{1})\D\W",file1[start1:end1])
print("no of degrees: ",len(nod))
data3=len(nod)
#resume_count=0
if  data3==0:
    resume_count=0
    resume_rank=0
    print("resume count for number_of_deg",resume_count)
    #print("resume rank is",resume_rank)

elif data3 <2:
    resume_count=resume_count+1
    resume_rank=resume_rank+1
    print("resume count for number_of_deg",resume_count)
    print("resume rank is",resume_rank)
elif data3 >=2:
    
    resume_count=resume_count+2
    resume_rank=resume_rank+2
    print("resume count for number_of_deg",resume_count)
    #print("resume rank is",resume_rank)
else:
    pass
    
print()

start3 = file1.find('ACADEMIC ACHIEVEMENTS & ACTIVITIES') 
end3 = file1.find('PERSONAL DETAILS')
str(file1[start3:end3])
no_of_achievements=re.findall(r"(\d{1,2}).\W\D",file1[start3:end3])
print("No of achievements are :",len(no_of_achievements))
data4=len(no_of_achievements)
#resume_count=0
if data4==0:
    resume_count=0
    resume_rank=0
    print("resume count for no_of_achievements",resume_count)
    #print("resume rank is",resume_rank)

elif data4 <5:
    resume_count=resume_count+1
    resume_rank=resume_rank+1
    print("resume count for no_of_achievements",resume_count)
    #print("resume rank is",resume_rank)
elif data4 >=5:
    resume_count=resume_count+2
    resume_rank=resume_rank+2
    print("resume count for no_of_achievements",resume_count)
    #print("resume rank is",resume_rank)
    
    print()

else:
    pass

print()

# add,data1,data2,maxim,data3,data4



maximum=maxim/9
newmax=round(maximum, 2)
final_li=[data1,newmax,0,data3,data2,data3,data4,0,0 ]    

#final_li.append(maximum)
#print("final list of outputs",final_li)



# Code to Find the Qualifiction and to rank it accordingly

f = open("C:/Users/neeraj/Desktop/mtech/cvs/7.txt", "r")
file2=f.read()
f.close()
x=str(file2)
#print(x)

start = x.find('EDUCATIONAL CREDENTIALS')
end = x.find('ACADEMIC ACHIEVEMENTS & ACTIVITIES')
newx=str(x[start:end])
#print(newx)

def qualification_rank():
    rank=0
    #global resumecounter
    dict_rank={"M-tech":8,"BE":7,"PGDBMB":7,"BCA":6,"MA":7,"MBA":7,"B.Com":5,"MCA":7,"B-SC":7,"MS":6}
    
    for key in dict_rank:
        if key in newx:
            value=dict_rank.get(key)
            print("value is ",value)
            print(key," element is present")
            rank=rank+value
            #print()
            print("total rank is ",rank)
            #print()
            if key is 'M-tech':
                mtech_cluster=[]
                mtech_cluster.append(key)
                print("key added in mtech cluster",mtech_cluster)
                
            if key is 'BE':
                be_cluster=[]
                be_cluster.append(key)
                print("key added in be cluster",be_cluster)
            if key is 'MBA':
                mba_cluster=[]
                mba_cluster.append(key)
                print("key added in mba cluster",mba_cluster)
            if key is 'BCA':
                bca_cluster=[]
                bca_cluster.append(key)
                print("key added in bca cluster",bca_cluster)
            
            if key is 'CA':
                ca_cluster=[]
                ca_cluster.append(key)
                print("key added in ca cluster",ca_cluster)

            if key is 'B.Com':
                bcom_cluster=[]
                bcom_cluster.append(key)
                print("key added in bca cluster",bcom_cluster)
            
            if key is 'MCA':
                mca_cluster=[]
                mca_cluster.append(key)
                print("key added in mca cluster",mca_cluster)

            if key is 'B-SC':
                bsc_cluster=[]
                bsc_cluster.append(key)
                print("key added in bsc cluster",bsc_cluster)
            
            if key is 'MS':
                ms_cluster=[]
                ms_cluster.append(key)
                print("key added in ms cluster",ms_cluster)

            print()

        elif key not in newx:
            pass
            #print(key ,"element not present")
            
qualification_rank()


