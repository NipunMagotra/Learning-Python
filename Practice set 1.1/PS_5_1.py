my_dict = {
    "Pankha ": "Fan",
    "rssi" : "Rope",
    "shiksha" : "Education",
    "ghanta": "Bell"
}
print("Options are: ", my_dict.keys())
a = input('Enter the hindi word\n')
print("The meaning of your word is",my_dict.get(a))