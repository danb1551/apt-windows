#### APT
###### But on Windows
###### So I name it
# WAPT

Did you ever think about apt on windows like in Linux? Yes, I did, and that’s why I started writing this code.

It's not alredy for use but you can look at it.

Web: [It's here (Just click)](https://wapt.pythonanywhere.com)

TODO:
- [ ] Make website look better
- [ ] Make better tools managing
- [x] Stop using "Make" and "better" words
- [ ] Upload it to the web


### How to make your own package?

Type
```bash
wapt [folder]
```
In your folder must be main.exe file. That's everything. But if your application requires more thing to run, everything in the folder will be uploaded (Max. folder size is 512MB). If you want to ignore some folders in root folder of you projekt, just type
```bash
wapt [folder] --ignore [folder-1, folder-2, ..., folder-n]
```

přidat spouštění aplikace po zadání příkazu
```bash
wapt [package-name-32/64bit]
```
výchozí bude 64bit

přidat tutoriál na deploying aplikací

```bash

./wapt
│
├──/App-1
├──/App-2
├──/App-3
├──/App-...
├──/App-n
└──/SETTING

```