import pprint
import setup, Debug_Class
import app


if __name__ == "__main__":
    setup.setup_check()
    #DL = Debug_Class.Debug_Log()
    #print('\n')
    #pprint.pprint(vars(DL))
    app.app.run()

