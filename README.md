# PABX_Aut-to_restart



#At my last job i had a task of checking if voice recording was activated twice a day.
#i fgured why not auotmate it. this program uses python and selenium to control a headless browser. the program logins into the PABX system, finds the correct page. Reads the html on that page to either do nothing or restart the service. It also emailed you if it went down. You could pretty much get it to do what you want.
#My Plan was to have this running on a windows system with task scheduler and have it run every few hours
