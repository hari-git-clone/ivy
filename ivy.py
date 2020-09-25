import os


while True:
    #start = input ("listening....")
    os.system ("termux-speech-to-text >> ivy.txt ")
    start = open("ivy.txt", "r")
    sta = start.read()
    print(sta) 
    st = sta.lower()
    os.remove()
    if sta in "ivy":
      print("yeah i am hear to help you all time..")
      command = input ('waitinng for your command>>>')
      cmd = command.lower()

      def hi():
        a = "hello"
        print(a)
        os.system(" termux-tts-speak " + a)

      def name():
        an = "my name is ivy.."
        print(an)
        os.system(" termux-tts-speak " + an)
      def about():
        ans = "Hi i am ivy , am a personal assistent, i make in python programming language, i developed by hari,i can able to do many this..my aim is helping make the work essayer")
        print(ans)
        os.system(" termux-tts-speak " + ans)

      def love():
        ans1 = "i love you too.."
        print(ans1)
        os.system(" termux-tts-speak " + ans1)
      def hate():
        ans2 = "i am besy with loveing others,i didn't have time to hate others.."
        print(ans2)
        os.system(" termux-tts-speak " + ans2)
      def torch_on():
        ans3 = "now the torch is on.."
        print(ans3)
        os.system(" termux-tts-speak " + ans3)
        os.system(" termux-toast NO")
        os.system(" termux-torch on")
      def torch_off():
        ans4 = "now the torch is off.."
        print(ans4)
        os.system(" termux-tts-speak " + ans4)
        os.system(" termux-toast OFF")
        os.system(" termux-torch off")
      def wifi_on():
        ans5 = "wifi is on now.."
        print(ans5)
        os.system(" termux-tts-speak " + ans5)
        os.system(" termux-toast WIFI-NO")
        os.system(" termux-wifi-enable true")
      def wifi_off():
        ans6 = "now the wifi is off.."
        print(ans6):
        os.system(" termux-tts-speak " + ans6)
        os.system(" termux-toast WIFI-OFF")
        os.system(" termux-wifi-enable fales")
      def vibrate():
        ans7 = "now it's vibrateing.."
        print(ans7)
        os.system(" termux-tts-speak " + ans7)
        os.system(" termux-toast vibrateing")
        os.system(" termux-vibrate ")
      
      if cmd in "hi":
        hi()
      elif cmd in "what is you name":
        name()
      elif cmd in "tell about you":
        about()
      elif cmd in "i love you":
        love()
      elif cmd in "torch on":
        torch_on()
      elif cmd in "torch of":
        torch_off()
      elif cmd in "vibrate":
        vibrate()
      elif cmd in "i hate you":
        hate()
      elif cmd in "wifi on"
        wifi_on()
      elif cmd in "wifi of"
        wifi_off()
