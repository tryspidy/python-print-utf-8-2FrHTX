# credit to the Stack Overflow user in the source link

TestText = "Test - āĀēĒčČ..šŠūŪžŽ" # this not UTF-8...it is a Unicode string in Python 3.X.
TestText2 = TestText.encode('utf8') # this is a UTF-8-encoded byte string.