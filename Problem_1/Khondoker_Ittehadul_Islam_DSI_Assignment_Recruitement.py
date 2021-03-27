import os
import warnings
import pandas as pd

class Display:

    def __init__ (self):

        self.path = 'products.csv'
        df = pd.read_csv(self.path)
        self.df = df
    
    
    def displayDf(self):

        """
        DESCRIPTION
        -------
        Prints Inherited Dataframe
        
        """

        df = self.df[self.df['Final'] == False]
        df = df[df['Delete'] == False]
        df = df.loc[:, df.columns != 'Final']
        df = df.loc[:, df.columns != 'Delete']
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)
        print(df)
    
    def show(self, df):
        """
        DESCRIPTION
        -------
        Prints Dataframe

        Argument
        -------
        df : Dataframe
        
        """
        print(df.to_string(index=False))
    
    def displayNotInheritedDf(self, df):

        """
        DESCRIPTION
        -------
        Prints Not Inherited Dataframe

        Argument
        -------
        df : Dataframe
        

        """


        df = df[df['Delete'] == False]
        df = df.loc[:, df.columns != 'Final']
        df = df.loc[:, df.columns != 'Delete']
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)
        print(df)
    

class SeeOverallInfo:
    def __init__(self):

        """
        DESCRIPTION
        -------
        Takes User's Query
        
        """
        self.path = 'products.csv'
        df = pd.read_csv(self.path)
        self.df = df
        self.val = int(input("See the overall info of:\n1. The total consumption time in hours across all types\n2. Individual consumption time in hours of each type\n3. The total days of consumption across all types\n4. Individual days of consumption of each type\n5. Average rating across all types\n6. Average individual rating of each type\n7. Total number of consumable across all types\n8. Individual number of consumable of each type\n Press the number of your query: "))
    
    def show(self):

        """
        DESCRIPTION
        -------
        Performs the User's Query and Displays the Result
        
        """

        if(self.val == 1):
            # Total Hrs Time Across Type
            print("The Total Consumption Time in Hours Across all types is " + str(self.df['Total Consumption (Hrs)'].sum()) + ' hrs')

        elif(self.val == 2):
            # Total Hrs Time Each Type
            print('Individual consumption time in hours of each type are: ')
            st = set(self.df['Type'].values)
            for item in st:
                df = self.df[self.df['Type'] == item]
                print(item + ' : ' , df['Total Consumption (Hrs)'].sum(), ' hrs')

        elif(self.val == 3):
            # Total Days Across Type
            print("The total days of consumption across all types: "+ str(self.df['Total Consumption (Days)'].sum()) + ' days' )

        elif(self.val  == 4):
            # Total Days Each Type
            print("Individual days of consumption of each type: ")
            st = set(self.df['Type'].values)
            for item in st:
                df = self.df[self.df['Type'] == item]
                print(item + ' : ' , df['Total Consumption (Days)'].sum() , ' days')

        elif(self.val == 5):
            # Average Across Type
            df = self.df[self.df['Delete'] == False]
            print("Average rating across all types: ", df['Rating'].mean())

        elif(self.val == 6):
            # Average each type
            df = self.df[self.df['Delete'] == False]
            st = set(df['Type'].values)
            for item in st:
                df1 = df[df['Type'] == item]
                print(item + ' : ' , df1['Rating'].mean())

        elif(self.val == 7):
            # Total Consums of All Type
            df = self.df[self.df['Delete'] == False]
            print("Total consumes: ", len(df), " products")

        elif(self.val == 8):
            # Total Consums of Each Type
            print("Total consumes of each type: ")
            df = self.df[self.df['Delete'] == False]
            st = set(df['Type'].values)
            for item in st:
                df1 = df[df['Type'] == item]
                print(item + ' : ' ,len(df1) , ' products')




class ShowConsumsIndividual:
    def __init__(self):

        self.path = 'products.csv'
        df = pd.read_csv(self.path)
        self.df = df
    
    def chooseTypeDisplay(self, types_dictionary):

        """
        DESCRIPTION
        -------
        Takes user's Type Input and Displays certain Column

        Arguement
        -------
        types_dictionary: Mapping of integer to the types
        
        """

        self.pro_type = int(input("Press the number corresponding to the type of product you want to add:\n1. Book\n2. Series\n3. Movies\n"))
        df = self.df[self.df['Type'] == types_dictionary[self.pro_type]]
        df = df[df['Delete'] == False]
        df = df[["Name", "Total Consumption (Days)", "Total Consumption (Hrs)", "Rating"]]
        display = Display()
        display.show(df)
    
    def seeProductDetail(self):

        """
        DESCRIPTION
        -------
        Takes user's Product Choice Input and Displays their Full Details
        
        """


        self.product_name = input("If you want to see a product detail, type the name of the product from the list: ")
        df = self.df[self.df['Type'] == types_dictionary[self.pro_type]]
        df = df[df['Name'] == self.product_name]
        display = Display()
        display.displayNotInheritedDf(df)
        
    

class Delete:
    def __init__(self):

        self.path = 'products.csv'
        df = pd.read_csv(self.path)
        self.df = df
    
    def chooseOption(self):

        """
        DESCRIPTION
        -------
        Takes user's Choice of Product Deletation
        
        """


        self.product_id = int(input("Type the Product_id you want to delete: ") )
    
    def displayDf(self):
        df = self.df[self.df['Delete'] == False]
        df = df.loc[:, df.columns != 'Final']
        df = df.loc[:, df.columns != 'Delete']
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)
        print(df)

    
    def implementOption(self):

        """
        DESCRIPTION
        -------
        Sets the Delete Columns as True and Deletes the row
        
        """

        for i in range(len(self.df)):
            if(self.df['Product ID'][i] == self.product_id):
                self.df['Delete'][i] = True
                break
        
        self.df.to_csv(self.path, index = False)
    
    



class Edit(Display):
    def __init__(self):

        self.path = 'products.csv'
        df = pd.read_csv(self.path)
        self.df = df
        

    def chooseOption(self):
        """
        DESCRIPTION
        -------
        Takes Input of User's Product ID and Asks for the Column to Edit
        
        """

        self.product_id = int(input("Type the Product_id you want to edit: ") )
        self.option = int(input("From the below options:\n1. Add hours of consumption\n2. Add days of consumption\n3. Edit the rating\n4. Add an end date of the consumption\nPress the number you want to edit: "))
    
    def implementOption(self):

        """
        DESCRIPTION
        -------
        Performs User's Edit Query and Updates the Value and Saves the New Dataframe
        
        """

        if(self.option == 1):
            for i in range(len(self.df)):
                if(self.df['Product ID'][i] == self.product_id):
                    self.df['Total Consumption (Hrs)'][i] += int(input("Enter the Hours you have read: "))
                    break


        elif(self.option == 2):
            for i in range(len(self.df)):
                if(self.df['Product ID'][i] == self.product_id):
                    self.df['Total Consumption (Days)'][i] += int(input("Enter the Days you have read: "))
                    break


        elif(self.option == 3):
            for i in range(len(self.df)):
                if(self.df['Product ID'][i] == self.product_id):
                    self.df['Rating'][i] = float(input("Change the rating of this consumption (Out of 10): "))
                    break


        elif(self.option == 4):
            for i in range(len(self.df)):
                if(self.df['Product ID'][i] == self.product_id):
                    self.df['Consumption Ending Date'][i] = input("Enter the end date of the consumption (YY-MM-DD): ")
                    self.df['Final'][i] = True
                    break



        self.df.to_csv(self.path, index = False)

class Add:
    type_name = ''
    name = ''
    start_date = ''
    end_date = ''
    total_consumption_hrs = 0
    rating = 0.0
    total_consumption_days = 0
    final_or_not = False
    delete_or_not = False


    def __init__(self,types, type_dic):
        self.type_name = type_dic[types]
    
    def nameInput(self):

        """
        DESCRIPTION
        -------
        Takes Mandoatory Name Column input from user
        
        """

        name = input("Input the name of product: ")
        if(len(name) == 0):
            print("Sorry, You have to provide a name!")
            return
        self.name = name
    
    def otherInput(self):

        """
        DESCRIPTION
        -------
        Takes Not-Mandatory Column's Input from User
        
        """

        start_date = input("\nInput the start date of this products' consumption (YY-MM-DD): ")

        self.start_date = start_date

        end_date = input("\nInput the end date of this products' consumption (YY-MM-DD): ")
        
        self.end_date = end_date

        total_consumption_hrs = input("\nInput the Total Consumption in Hrs: ")
        if(total_consumption_hrs.isdecimal()):
            self.total_consumption_hrs = int(float(total_consumption_hrs))
        else:
            self.total_consumption_hrs = 0


        rating = input("\nInput the rating of this consumption (Out of 10): ")
        # if(rating.isdecimal()):
        #     self.rating = float(rating)
        # else:
        #     self.rating = 0.0
        try:
            self.rating = float(rating)
        except:
            self.rating = 0.0

        total_consumption_days = input("\nInput the Total Consumption in Days: ")
        if(total_consumption_days.isdecimal()):
            self.total_consumption_days = int(float(total_consumption_days))
        else:
            self.total_consumption_days = 0
        

        if(len(end_date) > 0):
            self.final_or_not = True
    

    def saveInTable(self):

        """
        DESCRIPTION
        -------
        Updating the New Dataframe and Saving the New Dataframe
        
        """

        path = 'products.csv'
        df = pd.read_csv(path)
        row = []
        row.append(len(df)+1)
        row.append(self.type_name)
        row.append(self.name)
        row.append(self.start_date)
        row.append(self.end_date)
        row.append(self.total_consumption_hrs)
        row.append(self.rating)
        row.append(self.total_consumption_days)
        row.append(self.final_or_not)
        row.append(self.delete_or_not)

        final = []
        final.append(row)
        df1 = pd.DataFrame(final, columns = list(df))
        df = df.append(df1, ignore_index = True)
        

        df.to_csv(path, index = False)

class CreateTable:

    def __init__(self, name_of_types):
        self.name_of_types = name_of_types
    
    def generateTable(self):

        """
        DESCRIPTION
        -------
        Generating the dataframe and Specifying each column with their Corresponding Data Type
        
        """

        self.df = pd.DataFrame({'Product ID': pd.Series([], dtype='int'),
            'Type': pd.Series([], dtype='str'),
            'Name': pd.Series([], dtype='str'),
            "Consumption Starting Date": pd.Series([], dtype='str'),
            "Consumption Ending Date": pd.Series([], dtype='str'),
            'Total Consumption (Hrs)': pd.Series([], dtype='int'),
            'Rating': pd.Series([], dtype='float'),
            'Total Consumption (Days)': pd.Series([], dtype='int'),
            'Final': pd.Series([], dtype='bool'),
            'Delete': pd.Series([], dtype='bool')})
    
        self.df['Consumption Starting Date'] = pd.to_datetime(self.df['Consumption Starting Date'], format='%y-%m-%d')
        self.df['Consumption Ending Date'] = pd.to_datetime(self.df['Consumption Ending Date'], format='%y-%m-%d')
    

    def saveTable(self):

        """
        DESCRIPTION
        -------
        Saving the Dataframe
        
        """

        self.df.to_csv('products.csv', index = False)
    
    def getDictionary(self):

        """
        DESCRIPTION
        -------
        Creating Dictory of integer to Types
        
        RETURNS
        ------
        dic: Dictionary
        """

        dic = dict()
        for i in range(len(self.name_of_types)):
            dic[i+1] = self.name_of_types[i]

        return dic
        

if __name__ == '__main__':
    create_or_not = False
    warnings.filterwarnings("ignore")

    while(1):
        if(create_or_not == False):
            table = CreateTable(['book','series','movies'])
            create_or_not = True
            table.generateTable()
            table.saveTable()
            types_dictionary = table.getDictionary()

        val = int(input("What do you want to do?\n\n1. Add a consumable.\n2. Edit a consumable.\n3. Delete a consumable.\n4. See the list of consumables and individually.\n5. See overall info.\n6. Exit\n\nPress the number of your desired command: "))

        if(val == 6):
            break

        if(val == 1):

            add = Add(types = int(input("From the following types:\n1. Book\n2. Series\n3. Movies\nPress the number corresponding to the type of product you want to add: ") ), type_dic = types_dictionary )
            add.nameInput()
            add.otherInput()
            add.saveInTable()


        if(val == 2):

            edit = Edit()
            edit.displayDf()
            edit.chooseOption()
            edit.implementOption()


        if(val == 3):

            delete = Delete()
            delete.displayDf()
            delete.chooseOption()
            delete.implementOption()

        
        if(val  == 4):

            showIndiv = ShowConsumsIndividual()
            showIndiv.chooseTypeDisplay(types_dictionary = types_dictionary)
            showIndiv.seeProductDetail()


        
        if(val == 5):

            seeOverall = SeeOverallInfo()
            seeOverall.show()


            

