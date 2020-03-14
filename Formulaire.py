from tkinter import *
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


    def script_sql():
        index = 0
        for i in listUsers:
            script = 'INSERT INTO User (Name, LastName, Email, Promo) VALUES ("' + i[0] + '", "' + i[1] + '","' + i[2] + '","' + i[3] + '")'
            index += 1
            print(script)
        return


    # form validation button
    btnValidation = Button(frame, text='Valider', command=add_person)
    btnValidation.pack(side=LEFT)
    btnValidation.place(x="70", y="250")

    # button to send list to database scripting the request
    btnRequestDB = Button(frame, text='Script SQL', command=script_sql)
    btnRequestDB.pack(side=LEFT)
    btnRequestDB.place(x="380", y="250")


    window.mainloop()