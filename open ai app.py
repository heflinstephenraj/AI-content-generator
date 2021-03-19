from tkinter  import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser, requests
import openai
import tkinter.font as font


class MainApplication():
        

        def __init__(self, parent, *args, **kwargs):
                def callback(url):	
                        webbrowser.open_new(url)
                self.parent = parent
                
                parent.config(bg="red")
                s = ttk.Style()
                s.theme_create( "MyStyle", parent="alt", settings={"TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },"TNotebook.Tab": {"configure": {"padding": [50, 10],"background": "sky blue","font" : ('Comic Sans MS', '13', 'bold')},"map":       {"background": [("selected", "white")]},}})
                s.theme_use("MyStyle")
                parent.title("AI Content Generator")
                tabControl =  ttk.Notebook(parent)
                tab4 = ttk.Frame(tabControl)
                config_tab = ttk.Frame(tabControl)
                sample = ttk.Frame(tabControl)
                tab5 = ttk.Frame(tabControl)
                tabControl.add(tab4, text ='Demo')
                tabControl.add(sample, text ='Sample input') 
                tabControl.add(config_tab, text ='Configuration')
                tabControl.add(tab5, text ='About')
                tabControl.pack(expand = 1, fill ="both") 

                text_2_speech_info = ttk.Label(tab4,text="This is demo version.\nIn this app, We can use Open AI API to generate content.",justify=CENTER)
                text_2_speech_info["font"] = font.Font(family='Comic Sans MS', size=15, weight='bold')
                text_2_speech_info.pack()
                ttk.Label(tab4).pack()

                sample_title = ttk.Label(sample,text="Sample input.Try it in the demo",justify=CENTER)
                sample_title["font"] = font.Font(family='Comic Sans MS', size=15, weight='bold')
                sample_title.pack()
                ttk.Label(sample).pack()

                sample_text_box = Text(sample)
                copy_2_clip = Button(sample,text = "Copy to clipboard",  bg="yellow", command=lambda master=sample,sample_box=sample_text_box: self.copy_to_clip(master,sample_box))
                copy_2_clip["font"] = font.Font(family='Comic Sans MS', size=10,weight='bold')
                copy_2_clip.pack()
                ttk.Label(sample).pack()

                
                sample_text = "Blog topics for ecommerce Multivendor \n\n1. How fit a Multi-Vendor eCommerce Platform Right for Small Business?\n\n2. Know Your Ecommerce Marketplace Customers: What They Expect From You?\n\n3. Top 5 Reasons: Why B2B businesses Must Opt Online Marketplace Opportunity?\n\n4. Technical Features To Improve Your Multi-Vendor Marketplace Performance\n\n5. Magento 2 marketplace: Why One Should Give A Try?\n\n6. What Makes A Good Online Ecommerce Marketplace?\n\n7. How To Onboard And Make Your Online Marketplace Sellers Happy?\n\n8. Benefits and Challenges of Online Multi-Vendor Marketplace\n\n9. Why Invest In The B2B Ecommerce Marketplace and How Important It Is For You?\n\n10. Must-to have Features of the Magento B2B Marketplace\n\n11. Top 10 Ecommerce Marketplace Trends in 2021\n\n12. Top 5 Reasons Retailers Need to Launch Their Own Online Marketplace\n\n13. Why you should integrate your eCommerce store with a Marketplace?\n\n14. What Are Online Marketplaces And Their Types And Future\n\n15. 4 Features Of Magento Marketplace Mobile App To Boost Your Ecommerce Business\n\n16. Multi-vendor Ecommerce Script: How to pick the right one?\n\n17. How to Choose the Best Ecommerce Marketplace Platform for your Business?\n\n18. What are the Benefits of Multi-Vendor Marketplace?\n\n19. The Top 5 Reasons Why You Should Create an Online Marketplace\n\n20. Why You Need to Start an Online B2B Marketplace?\n\n21. How to Improve Your Online Marketplace Product Listing?\n\n22. How to Select the Best Ecommerce Marketplace Platform for your Business?\n\n23. What are the Benefits of Multi-Vendor Marketplace?\n"
                sample_text_box.insert(INSERT, sample_text)
                sample_text_box.config(state=DISABLED)
                sample_text_box.pack(expand=1, fill=Y)


                input_text_box = Text(tab4)
                text_box = Text(tab4)
                

                convert_txt_2_sph = Button(tab4,text = "Generate",  bg="yellow", command=lambda master=tab4,insert_box=input_text_box,write_=text_box: self.generate(master,insert_box,write_))
                convert_txt_2_sph["font"] = font.Font(family='Comic Sans MS', size=10,weight='bold')
                convert_txt_2_sph.pack()

                copy_2_clip_output = Button(tab4,text = "Copy the output to clipboard",  bg="yellow", command=lambda master=sample,sample_box=text_box: self.copy_to_clip(master,sample_box))
                copy_2_clip_output["font"] = font.Font(family='Comic Sans MS', size=10,weight='bold')
                ttk.Label(tab4,text="").pack()
                copy_2_clip_output.pack()

                ttk.Label(tab4).pack()
                clear_button = Button(tab4,text = "Clear",  bg="yellow", command=lambda master=tab4,insert_box=input_text_box,write_=text_box: self.clear(master,insert_box,write_))
                clear_button["font"] = font.Font(family='Comic Sans MS', size=10,weight='bold')
                clear_button.pack()

                ttk.Label(tab4).pack()
                about_the_app = ttk.Label(tab5,text="\nThis is AI Content Generator Desktop App.\nThis app use Open AI to generate the content.\nThis app is developed by Heflin Stephen Raj S.\n",justify=CENTER)
                about_the_app["font"] = font.Font(family='Comic Sans MS', size=13,weight='bold')
                about_the_app.pack()
                contact = ttk.Label(tab5,text="Contact me",justify=CENTER,cursor="hand2",foreground="blue")
                contact["font"] = font.Font(family='Comic Sans MS', size=13,weight='bold',underline=True)
                contact.bind("<Button-1>", lambda e: callback("https://www.heflin.dev/"))
                contact.pack()
                
                input_title = ttk.Label(tab4,text="Input"+" "*90 +"Output")
                input_title["font"] = font.Font(family='Comic Sans MS', size=15,weight='bold')
                input_title.pack()

                ttk.Label(tab4,text=" "*7).pack(side=LEFT)
                ttk.Label(tab4,text=" "*7).pack(side=RIGHT)
                
                input_text_box.insert(INSERT, "Enter the text here....")
        
                input_text_box.pack(side=LEFT)

                text_box.insert(INSERT, "Generated text will appear here..")
                text_box.config(state=DISABLED)
                text_box.pack(side=RIGHT)
                
                thank = ttk.Label(tab5, text= "\nThank you for using my app.",justify=CENTER)
                thank['font']=font.Font(family='Comic Sans MS', size=13,weight='bold')
                thank.pack()

                #config
                global v2
                randomness = ttk.Label(config_tab, text= "\nRandomness:",justify=CENTER)
                randomness_define = ttk.Label(config_tab, text= "Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.\nRecom",justify=CENTER)
                randomness_define['font']=font.Font(family='Comic Sans MS', size=13)
                randomness['font']=font.Font(family='Comic Sans MS', size=13,weight='bold')
                v2 = DoubleVar()
                s2 = Scale( config_tab, variable = v2, from_ = 0, to = 100, orient = HORIZONTAL)
                randomness.pack()
                randomness_define.pack()
                s2.pack()

                global v1
                consider = ttk.Label(config_tab, text= "\nContent accuracy consideration:",justify=CENTER)
                consider['font']=font.Font(family='Comic Sans MS', size=13,weight='bold')
                consider_define = ttk.Label(config_tab, text= "Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered.",justify=CENTER)
                consider_define['font']=font.Font(family='Comic Sans MS', size=13)
                v1 = DoubleVar()
                s1 = Scale( config_tab, variable = v1, from_ = 0, to = 100, orient = HORIZONTAL)
                consider.pack()
                consider_define.pack()
                s1.pack()

                global v3
                frequency_in = ttk.Label(config_tab, text= "\nInput frequency:",justify=CENTER)
                frequency_in['font']=font.Font(family='Comic Sans MS', size=13,weight='bold')
                frequency_in_define = ttk.Label(config_tab, text= "How much to penalize new tokens based on their existing frequency in the text so far. Decreases the model's likelihood to repeat the same line verbatim.",justify=CENTER)
                frequency_in_define['font']=font.Font(family='Comic Sans MS', size=13)
                v3 = DoubleVar()
                s3 = Scale( config_tab, variable = v3, from_ = 0, to = 100, orient = HORIZONTAL)
                frequency_in.pack()
                frequency_in_define.pack()
                s3.pack()

                global v4
                frequency_out = ttk.Label(config_tab, text= "\nOutput frequency:",justify=CENTER)
                frequency_out_define = ttk.Label(config_tab, text= "How much to penalize new tokens based on whether they appear in the text so far. Increases the model's likelihood to talk about new topics.",justify=CENTER)
                frequency_out_define['font']=font.Font(family='Comic Sans MS', size=13)
                frequency_out['font']=font.Font(family='Comic Sans MS', size=13,weight='bold')
                v4 = DoubleVar()
                s4 = Scale( config_tab, variable = v4, from_ = 0, to = 100, orient = HORIZONTAL)
                frequency_out.pack()
                frequency_out_define.pack()
                s4.pack()


                try:
                        data = requests.get("https://www.google.com").status_code
                except:
                        check = messagebox.showwarning("Connection error", "Please check your internet connectivity.\nSmart classify needs proper internet connection to run")
                        if check == "ok":
                                parent.destroy()

            
        def copy_to_clip(self,master,input_box):
                text = input_box.get("1.0", "end-1c")
                master.clipboard_clear()
                master.clipboard_append(text)
                messagebox.showinfo("AI Content Generator", "Copied to clipboard.") 

        def clear(self,master,input_box,output_box):
                
                output_box.config(state=NORMAL)
                output_box.delete(1.0,END)
                output_box.insert(INSERT, "Generated text will appear here..")
                output_box.config(state=DISABLED)
                input_box.delete(1.0,END)
                input_box.insert(INSERT, "Enter the text here....")



        def generate(self,master,input_box,output_box):
                output_box.config(state=NORMAL)
                openai.api_key = "" #Paste your Open AI API Key here
                #text_file = askopenfilename(filetypes=[("text file","*.txt")])
                #with open(text_file) as text_data:
                        #text = text_data.read()
                
                text = input_box.get("1.0", "end-1c")
                output_text = output_box.get("1.0", "end-1c")
 
                if output_text == "Generated text will appear here..":
                        pass
                else:
                        text=text+output_text

                output_box.delete(1.0,END)
                random_value=float(str(v2.get()/100)[:3])
                consider_value=float(str(v1.get()/100)[:3])
                frequency_in_value=float(str(v3.get()/100)[:3])
                frequency_out_value=float(str(v4.get()/100)[:3])
                print(f"random_value: {random_value}\nconsider_value: {consider_value}\nfrequency_in_value: {frequency_in_value}\nfrequency_out_value: {frequency_out_value}")
                print("-"*5)
                response = openai.Completion.create(engine="davinci",prompt=text,temperature=random_value,max_tokens=64,top_p=consider_value,best_of=80,frequency_penalty=frequency_in_value,presence_penalty=frequency_out_value)
                result=response.to_dict_recursive()
                final_text = result["choices"][0]["text"]
                
                global result_text
                try:
                        result_text = result_text + final_text
                except:
                        result_text = final_text
                output_box.insert(INSERT, result_text)
                              
                

if __name__ == "__main__":
    root = Tk()
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    MainApplication(root)
    root.mainloop()