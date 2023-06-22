#Fayllar bilan ishlash
#1.Creat (Yaratish)
#2.Update (Yangilash)
#3.Read (O'qish)
#4.Delete (O'chirish)

#1-read "r"
#2-write "w"
#3-append "a"
#4-create "x"
#5-Banner "b"
#6-text "t"
#7-Update "+"



# 1-Oqib olish
# file1 = open('demofile.txt','r')
# faylni_uqish = file1.read()
# print(faylni_uqish )

# with open('demofile.txt','r') as fayl1:
#         read_text = fayl1.read()
#         print(read_text)

# 2-qayerdaligini topish
# import os
# print(os.getcwd())


# try:
#     file1 = open('demofile.txt','r')
#     faylni_uqish = file1.read()
#     print(faylni_uqish )
# except:
#     file1.close()

#Fayllar bilan ishlash ('w' -> write rejim)
# with open('demofile.txt','w') as yangi_file:
#     yangi_file.write("Salom bolla")
# with open('demofile.txt','r') as fayl1:
#         read_text = fayl1.read()
#         print(read_text)


#Fayllar bilan ishlash ('a' -> append rejim)

# with open('demofile.txt','a') as fayl1:
#         fayl1.write("\t hayr bolla.")


#Fayllar bilan ishlash ('a and w' -> creat rejim)
# with open('demofile3.txt','w') as yangi_file:
#     yangi_file.write("\n sdalom bolla")


#Fayllar bilan ishlash ('x' -> creat rejim)
# f = open('demofile4.txt','x')


#Fayllarni ochirish 
import os
# os.remove('demofile4.txt')
print(os)