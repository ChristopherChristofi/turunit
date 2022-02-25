import os, sys, getopt

class Workman:

    clock_off = 0

    def get_opts(self, args):
        self.args = args
        try:
            opts, argvs = getopt.getopt(self.args,"iep:", ["printit="])
            self.parse_opts(opts)
        except getopt.GetoptError:
            print("python3 turunit.py -i <info> -p <printit> -e <exit>")
            sys.exit(2)

    def parse_opts(self, options):
        for opt, arg in options:
            if opt == '-i':
                print("python3 turunit.py -i <info> -p <printit> -e <exit>")
                sys.exit()
            elif opt in ['-p', '--printit']:
                os.system(arg)
            # exit option
            elif opt == '-e':
                self.clock_off = 1

class TurunitDaemon(Workman):

    def __init__(self, sleep, workload):
        self.sleep = sleep
        self.workload = workload

    def listening(self):
        self.sleep and self.go_sleep() or not self.sleep and self.use_hands()

    def use_hands(self):
        print("Hands")
        self.get_opts(args=self.workload)
        self.sleep = self.clock_off
        if self.sleep:
            self.listening()
        if not self.sleep:
            self.get_opts(args=self.workload)
            #self.listening()   - inifinity loop

    def go_sleep(self):
        print("Goodnight")

if __name__ == "__main__":

    listen = sys.argv[1:]
    #argelems = 1
    if listen: TurunitDaemon(sleep=False, workload=listen).listening()
