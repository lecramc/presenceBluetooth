from tkinter import *
import pymysql
#import Formulaire
con = pymysql.connect('localhost', 'root', '', 'bluetooth')


def commit(monCurseur, maVar):
    try:
        monCurseur.execute(maVar)
        con.commit()
    finally:
        con.close()

def select(sql):
    with con.cursor() as cursor:
        cursor.execute(sql)
        return cursor.fetchall()

def get_last_id():
    last_id = "SELECT LAST_INSERT_ID() FROM Appel"
    return last_id

def FenMain(device):

    listDevice = device

    MaFenetre = Tk()
    MaFenetre.title("APPEL")
    MaFenetre.geometry("400x400")


    UserPLabel = Label(MaFenetre, text="Présent :")
    UserPLabel.place(x="0", y="30")

    UserALabel = Label(MaFenetre, text="Absent :")
    UserALabel.place(x="210", y="30")

    addrMac = Label(MaFenetre)
    addrMac.place(x="210", y="35")

    ListUserP = Listbox(MaFenetre)
    ListUserP.place(x="2", y="55")

    ListUserA = Listbox(MaFenetre)
    ListUserA.place(x="210", y="55")

    def get_list_user(listDevice):
        sql = "SELECT IDDevice, User.IDUser, MacAddr, User.Name, User.LastName FROM `Device` LEFT JOIN User ON Device.IDDevice = User.IDUser "
        list = select(sql)
        #isOK = False
        print(list)
        for j in list:
            isOK = False
            for i in listDevice:
                if i[1] == j[2]:
                    ListUserP.insert(ListUserP.size(), j[4] + ' ' + j[3])
                    isOK = True
            if isOK == False:
                ListUserA.insert(ListUserA.size(),j[3]+' ' + j[4])



    def formulaireEleve():
        Formulaire()



    def SendMail():
        index = 0
        cursor = con.cursor()
        for i in ListUserA:
            script = 'INSERT INTO Presence (IDAppel, IDUser) VALUES ("' + get_last_id() + '", "' + i[1] + '")'
            commit(cursor, script)
            index += 1
            print(script)


    button = Button(MaFenetre, text="Ajouter un nouveau device", command= lambda: NewUserDevice(listDevice))
    button.place(x="200", y="0")

    FormInscrit = Button(MaFenetre,text="Formulaire Inscription", command=formulaireEleve)
    FormInscrit.place(x="0",y="0")

    SendMail = Button(MaFenetre,text="Valider et Envoyer le mail", command=SendMail)
    SendMail.place(x="110",y="250")

    #get_list_user(nameD)

    MaFenetre.mainloop()

def NewUserDevice(listDevice):
    window = Tk()
    window.title('Hello Clément')
    window.geometry('500x400')

    frame = Frame(window, bg="#2B2B2B", width=650, height=400)
    frame.pack()

    titleLabel = Label(frame, text="Devices & Names to SQL Database", bg="#2B2B2B", font=('Helvetica', 20),
                       fg="#1A90DB")  # flat/groove/raised/ridge/solid/sunken
    titleLabel.pack(side=LEFT)
    titleLabel.place(x="40", y="5")
    IndexDevice = 0
    IndexUser = 0

    listDevice = listDevice
    listUser = select("SELECT * FROM User")


    # Creation listBox 1 (Devices names) + Scroll
    yDefilBoxLeft = Scrollbar(frame, orient='vertical')
    xDefilBoxLeft = Scrollbar(frame, orient='horizontal')

    listBoxLeftLabel = Label(frame, text="Devices Names :", bg="#2B2B2B", fg="#1A90DB", font=("Helvetica", 15))
    listBoxLeftLabel.pack(side=LEFT)
    listBoxLeftLabel.place(x="10", y="40")

    listBoxLeft = Listbox(frame, width=20, height=10, xscrollcommand=xDefilBoxLeft.set,
                          yscrollcommand=yDefilBoxLeft.set, bg="#b4abab")
    listBoxLeft.pack(side=LEFT)
    listBoxLeft.place(x="10", y="70")

    xDefilBoxLeft['command'] = listBoxLeft.xview
    yDefilBoxLeft['command'] = listBoxLeft.yview

    # Creation listBox 2 (User names) + Scroll
    yDefilBoxRight = Scrollbar(frame, orient='vertical')
    xDefilBoxRight = Scrollbar(frame, orient='horizontal')

    listBoxRightLabel = Label(frame, text="User Names :", bg="#2B2B2B", fg="#1A90DB", font=("Helvetica", 15))
    listBoxRightLabel.pack(side=LEFT)
    listBoxRightLabel.place(x="300", y="40")

    listBoxRight = Listbox(frame, width=20, height=10, xscrollcommand=xDefilBoxRight.set,
                           yscrollcommand=yDefilBoxRight.set, bg="#b4abab")
    listBoxRight.pack(side=LEFT)
    listBoxRight.place(x="300", y="70")

    xDefilBoxRight['command'] = listBoxRight.xview
    yDefilBoxRight['command'] = listBoxRight.yview

    # Creation listBox 3 (Concatenation devices + names) + Scroll
    yDefilBoxBottom = Scrollbar(frame, orient='vertical')
    xDefilBoxBottom = Scrollbar(frame, orient='horizontal')

    listBoxBottomLabel = Label(frame, text="User Names :", bg="#2B2B2B", fg="#1A90DB", font=("Helvetica", 15))
    listBoxBottomLabel.pack(side=LEFT)
    listBoxBottomLabel.place(x="10", y="270")

    listBoxBottom = Listbox(frame, width=53, height=3, xscrollcommand=xDefilBoxBottom.set,
                            yscrollcommand=yDefilBoxBottom.set, bg="#b4abab")
    listBoxBottom.pack(side=LEFT)
    listBoxBottom.place(x="10", y="295")

    xDefilBoxBottom['command'] = listBoxBottom.xview
    yDefilBoxBottom['command'] = listBoxBottom.yview

    def clicDevice(evt):
        global IndexDevice
        IndexDevice = listBoxLeft.curselection()[0]  ## DEVICE
        print(IndexDevice)  ## On retourne l'élément (un string) sélectionné

    def clicUser(evt):
        global IndexUser
        IndexUser = listBoxRight.curselection()[0]  ## USER
        print(IndexUser)  ## On retourne l'élément (un string) sélectionné

    listBoxLeft.bind('<1>', clicDevice)
    listBoxRight.bind('<1>', clicUser)  ## on associe l'évènement "relachement du bouton gauche la souris" à la listbox

    # listDevice = ["BT05", "BT06", "BT07"]
    # listUser = ["Mathieu", "Clement", "Gabriel"]
    #
    # def addListDevice():
    #     listBoxLeft.delete(0, 'end')
    #     #indexDevice = 0
    #
    #     for i in listDevice:
    #         listBoxLeft.insert(listBoxLeft.size(), i[2] + ' ' + i[1])
            #indexDevice += 1

    def addListUser():
        listBoxRight.delete(0, 'end')
        #indexUser = 0

        for i in listUser:
            listBoxRight.insert(listBoxRight.size(), i[3] + ' ' + i[4])
            #indexUser += 1

    TableauRelation = []

    def scanDevice(listDevice):
        for i in listDevice:
            listBoxLeft.insert(listBoxLeft.size(), str(i[0]) + ' ' + i[1])

    def addListRelation():
        print(str(IndexDevice) + " / " + str(IndexUser))
        DeviceValue = str(listDevice[IndexDevice][1])
        UserValue = str(listUser[IndexUser][3])
        MaChaine = DeviceValue + " " + UserValue
        listBoxBottom.insert(listBoxBottom.size(), MaChaine)

    # Concatenation Button
    btnValidationDeviceName = Button(frame, text='Create', command=addListRelation, width=7)
    btnValidationDeviceName.pack(side=LEFT)
    btnValidationDeviceName.place(x="180", y="250")
    btnValidationDeviceName.config(font=("Helvetica", 15), bg='#1A90DB', fg='white', highlightbackground="#2B2B2B")

    # Script SQL button
    btnScriptSQL = Button(frame, text='Script SQL', command="", width=9)
    btnScriptSQL.pack(side=LEFT)
    btnScriptSQL.place(x="175", y="360")
    btnScriptSQL.config(font=("Helvetica", 15), bg='#1A90DB', fg='white', highlightbackground="#2B2B2B")

    #addListDevice()
    addListUser()
    scanDevice(listDevice)
    window.mainloop()

def Formulaire():
    window = Tk()
    window.title('HelloMathieu')
    window.geometry('650x300')

    frame = Frame(window, bg="lightgrey", width=650, height=300, )
    frame.pack()


    # Creation label lastname and entry name
    lastnameLabel = Label(frame, text="Nom : ", bd=0, bg="lightgrey")
    lastnameLabel.pack(side=LEFT)
    lastnameLabel.place(x="10", y="5")

    lastnameEntry = Entry(frame, bd=0)
    lastnameEntry.pack(side=LEFT)
    lastnameEntry.place(x="10", y="30")

    # Creation label firstname and entry name
    firstnameLabel = Label(frame, text="Prenom : ", bd=0, bg="lightgrey")
    firstnameLabel.pack(side=LEFT)
    firstnameLabel.place(x="10", y="65")

    firstnameEntry = Entry(frame, bd=0)
    firstnameEntry.pack(side=LEFT)
    firstnameEntry.place(x="10", y="90")

    # Creation label email and entry name
    emailLabel = Label(frame, text="E-mail : ", bd=0, bg="lightgrey")
    emailLabel.pack(side=LEFT)
    emailLabel.place(x="10", y="125")

    emailEntry = Entry(frame, bd=0)
    emailEntry.pack(side=LEFT)
    emailEntry.place(x="10", y="150")

    # #Creation label promo and entry name
    promoLabel = Label(frame, text="Promo : ", bd=0, bg="lightgrey")
    promoLabel.pack(side=LEFT)
    promoLabel.place(x="10", y="185")

    promoEntry = Entry(frame, bd=0)
    promoEntry.pack(side=LEFT)
    promoEntry.place(x="10", y="210")


    # Creation listBox
    yDefilBox = Scrollbar(frame, orient='vertical')
    xDefilBox = Scrollbar(frame, orient='horizontal')

    listBoxLabel = Label(frame, text="Résultat du formulaire :", bd=0, bg="lightgrey")
    listBoxLabel.pack(side=LEFT)
    listBoxLabel.place(x="247", y="5")

    listBox = Listbox(frame, width=40, xscrollcommand=xDefilBox.set, yscrollcommand=yDefilBox.set)
    listBox.pack(side=LEFT)
    listBox.place(x="250", y="30")

    xDefilBox['command'] = listBox.xview
    yDefilBox['command'] = listBox.yview

    listUsers = []


    # clear form
    def clear_form():
        lastnameEntry.delete(0, 'end')
        firstnameEntry.delete(0, 'end')
        emailEntry.delete(0, 'end')
        promoEntry.delete(0, 'end')


    # add form values to the list
    def add_person():
        lastnameValue = lastnameEntry.get()
        firstnameValue = firstnameEntry.get()
        emailValue = emailEntry.get()
        promoValue = promoEntry.get()
        user = (lastnameValue, firstnameValue, emailValue, promoValue)
        listUsers.append(user)
        clear_form()
        insert_data_list()



    def insert_data_list():
        index = 0
        listBox.delete(0, 'end')
        for i in listUsers:
            formChain = "Nom : " + i[0] + " Prénom : " + i[1] + " E-mail : " + i[2] + " Promo : " + i[3]
            listBox.insert(index, formChain)
            index += 1


    def sql_user():
        index = 0
        cursor = con.cursor()
        for i in listUsers:
            script = 'INSERT INTO User (Name, LastName, Email, Promo) VALUES ("' + i[0] + '", "' + i[1] + '","' + i[2] + '","' + i[3] + '")'
            commit(cursor, script)
            index += 1
            print(script)

    def delete_ligne():
        cursorselection = listBox.curselection()
        listBox.delete(cursorselection[0])
        listUsers.pop(cursorselection[0])
        return

    # form validation button
    btnValidation = Button(frame, text='Valider', command=add_person)
    btnValidation.pack(side=LEFT)
    btnValidation.place(x="70", y="250")

    # button to send list to database scripting the request
    btnRequestDB = Button(frame, text='Script SQL', command=sql_user)
    btnRequestDB.pack(side=LEFT)
    btnRequestDB.place(x="230", y="250")

    # button to delete ligne from list
    btnRequestDB = Button(frame, text='Delete Ligne', command=delete_ligne)
    btnRequestDB.pack(side=LEFT)
    btnRequestDB.place(x="330", y="250")

    window.mainloop()

