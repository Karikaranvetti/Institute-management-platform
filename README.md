# Institute-management-platform-
this a web app that's managing institute staff and students details and market their services 
# Smart Vending Machine

**Hello everyone!! Welcome to My project.**  

 ![top](https://github.com/Karikaranvetti/Institute-management-platform/blob/main/Doc/pic1.png)

[**Click here to check our deployed website!!**](https://new-success-college.herokuapp.com/)
 

## Contact Me
   
   
   > [V Harikaran](https://github.com/Karikaranvetti)  :: e16172@eng.pdn.ac.lk
   
 
   
   
    
 
 ## PROBLEMS
   Lack of 24 hrs Open Shops.MRP products sold for higher prices.Having a big space for a shop.Having to pay for the products with cash most of the time.Easy to hack Traditional vending machine.Prices and Expiry dates are not checked by the  Traditional vending machine.
    ![problems](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/COMPARISON-FA-01.jpg)
     


 ## OVERVIEW
  In Smart vending machine we are addresiing the problems faced by the companies and the Consumers in communication and 
  transaction. We hope to give a real time analysis of the market for each and every product available in the vending machine.
  
![overview](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/show2.png)

  The software architecture works like the above mentioned picture First user accesses the web application and he chooses the products and the interface was made by the Python Django and the details are updated in to the database which is made by MongoDB And it is al so in the server which is The Amazon EC3 instance All the communications are done through https. There is an API in the machine which connects the sever to get the Validation requests.Finally the Machine dispences the item chose by the user
  
  
 ## SOLUTIONS
  Problems in having a traditional vending machine are - Having to pay for the products with cash most of the time.Easy to hack Traditional vending machine.Prices and Expiry dates are not checked by the Traditional vending machine.

![overview](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/show1.png)
the solution to all the problem is a Smart vending machine which has the (Gender ,Age ,generation wise) analysis , 24 hours Distribution and vending services , Transaction Datbase services. Which can be used to check the performance of a product in a specific market.Prices and expiry dates are real time because it is connected to the cloud.
 

  
 ## TECHNOLOGIES
  ### Cashless payments																
   * Using mobil e payment methods and  Card Transaction .
  ### Smartphone interaction																
   * Using smart phones to selection of the products , using the money transfer systems		
     like the help of google wallet.
  ### Energy-Saving Vending															
   * Making sure the vending machine only works when a customers there. 
     Minor changes can be made to ensure energy saving.

##   SOFTWARE  
  ### Back End Tasks Done
#### User Registration (User /Admin/Companies)
Where users are classified into who they are according to their Credential. These Roles can determine the access given to a selected user.
#### Payment Handling

Payment Handling is done through PayPal Which is a secured Payment Gateway
#### Add /Modify/Delete Items

The admin can Edit any information about the items available
#### Validation

QR code is used for more security and also Django Rest API is used for validity
#### Transactions

Every Transaction Done can be Seen by an admin .The User can also see the previous Transactions done by him.


### Server
Local server is made using Python Django

The database is made in PostGreSQL

Communication to AWS is done through HTTPS 

### Cloud Server

 Host in amazon EC2 Instance

Nginix Server is used because Nginx is built to offer low memory usage and high concurrency. Rather than creating new processes for each web request, Nginx uses an asynchronous, event-driven approach where requests are handled in a single thread. With Nginx, one master process can control multiple worker processes.

Gunicorn is used and it internally hands the calling of our flask code. This is done by having workers ready to handle the requests instead of the sequential one-at-a-time model that the default flask server provides. The end result is our app can handle more requests per second

Built with Python Django

Used database PostGreSQL 

### Rest API

To authenticate we are using JSON web token because it securely transfers information between software and Hardware as an JSON file.It has 2 tokens one is access token which expires within 5 minutes . We are using Rate limit to make sure the hardware/Web Application does not get overloaded by API calls to the cloud and it is only 60 API calls per hour.It ensure the safety of the systems.We can do GET,PUT,POST,DELETE in the APIs that are available in the system. 

## INTERFACE

 ### Online Demonstration Video
 [![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/h6RIBUuqOs0/0.jpg)](https://www.youtube.com/watch?v=h6RIBUuqOs0)
 
 
 
![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/ui1.jpeg)
  The Website gets you to this Home page which Can be used to directly buy items or you can sign in and buy things If you sign in the company can give you discounts or other options.And also from the Homepage you can go to the cart which has the items you selected and the total amount.Other than that you can also go to the tab pending orders and use the QR codes to get the paid items to dispense. 

  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/ui2.jpeg)
  This Page is the page you get if you want to Login.You can type in your login credentials and get into the account where you can see your previous orders and etcs. Or If you don't have an account you can go to the Signup option and Sign up for a new account.There is an option to help you reset your password as well if you forget. 

  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/signup.jpeg)
  This is the SignUp page where you can Sign up for a new Account.The creditentials can be created here and there is a email checker and the email should be legitimate to sign in 
  
  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/ui2.jpeg)
  After Signing in you will have a page similar to the home page but you can see your account and you can make changes to your account when you click on your profile picture.And also you will have an Profile Button on your webpage where you can go and change your account settings. 
  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/cartview.jpeg)
  After you added the items your Cart the cart looks like this and you can edit the items that you are going to add here also.If you click check out it will take to a page where your can pay for the Items.You can use continue shopping to go back and add more items to the cart.
  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/payment.jpeg)
  When you go to the checkout page you can see that it will ask for a name and an email. It is just for the invoice so you can use it for refunds and other proceeds. 
  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/payways.jpeg)
  After giving the Email and the name You can choose the way to pay (Paypal / Debit Card /Credit card).After choosing the payment method you will be redirected to a dialog box which is going popup and you can give your details there and pay for the items and you will receive the items. 

  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/paypal.jpeg)
    pop up will redirect you to Paypal

  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/admindata.jpeg)
  If you Login with the admin Credentials you can see all the transactions that have happened with the vending machine over the time. And you can check who has bought the items and their characteristics according to their accounts.And also you can check the pending transactions. 
  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/productadd.jpeg)
  If you Login as an Admin You can also change the number of products in the vending machine.If you see any miscalculations. And also you can search for items according to their places and the prices and also the names. 
  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/OrderQR.jpeg)
  The other page you can check are the QR codes of the customers who are going to buy the items. 

 

 
  
  

 ## TESTING
 
  ### URL unit Testing
   * This test was done in order to check whether the end to end data transaction is happening or not.   
   
   ![testing](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/test1.png)
  
  ### POST/GET Request unit Testing
   * This test to check the post and get requests
   
   ![testing](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/test2.png)
   ![testing](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/test3.png)
  
 
   * This test to check the Forms
   
   ![testing](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/test4.png)
   
 
  
