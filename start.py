# f = open("/Users/jp/PY4E/doit/새파일.txt", 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# f = open("/Users/jp/PY4E/doit/새파일.txt", 'r')
# line = f.readline()
# print(line)
# f.close()



# f = open("/Users/jp/PY4E/doit/새파일.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     line = line.strip()
#     print(line)
# f.close()



# f = open("/Users/jp/PY4E/doit/새파일.txt", 'a')
# for i in range(11,20):
#     data = "%d번째 줄입니다.\n" % i 
#     f.write(data)
# f.close()


# f = open("foo.txt", 'w')
# f.write("Life is too short, you need python")
# f.close()

with open("foo.txt", "w") as f :
    f.write("Life is too short, you need python")
