loan_default <-read.table("loan_default.csv", header=TRUE, sep=",")
loan_default <- loan_default[ ,-c(2,3,8,20,23,25,27,29,32,33)] 
summary(loan_default) 

#VALUES 
gender <- loan_default[2] 
approv_in_adv <- loan_default$approv_in_adv 
loan_type <- loan_default$loan_type 
loan_purpose <- loan_default$loan_purpose 
business_or_commercial <- loan_default$business_or_commercial 
loan_amount <- loan_default$loan_amount 
rate_of_interest <- loan_default$rate_of_interest 
income <- loan_default$income 
term <- loan_default$term 
property_value <- loan_default$property_value 
age <- loan_default$age 
credit_score <- loan_default[20] 
LTV <- loan_default$LTV 
region <- loan_default$Region 
interest_rate_spread <- loan_default$Interest_rate_spread 
dtir1 <- loan_default$dtir1 
open_credit <- loan_default$open_credit 
upfront_charges <- loan_default[11] 
neg_ammortization <- loan_default[13] 
interest_only <- loan_default$interest_only 
lump_sum_payment <- loan_default$lump_sum_payment 
occupancy_type <- loan_default$occupancy_type 
secured_by <- loan_default[18]  

#TABLES BY VARIABLES 
table(age) 
table(loan_type) 
table(loan_purpose) 
table(business_or_commercial) 
table(gender) 
table(credit_score)   

#AVERAGE OF NUMERIC VALUES 
mean(income) 
mean(term) 
mean(loan_amount) 
mean(property_value)
mean(rate_of_interest) 
mean(interest_rate_spread) 
mean(credit_score) 
mean(LTV) 
mean(dtir1) 
mean(upfront_charges)  

#MAX/MIN 
table(age) 
which.max(table(age)) 
which.min(table(age))  
table(loan_type) 
which.max(table(loan_type)) 
which.min(table(loan_type))  
table(loan_purpose) 
which.max(table(loan_purpose)) 
which.min(table(loan_purpose))  
table(business_or_commercial) 
which.max(table(business_or_commercial)) 
which.min(table(business_or_commercial))  
table(gender) 
which.max(table(gender)) 
which.min(table(gender))  
table(credit_score) 
which.max(table(credit_score)) 
which.min(table(credit_score))  

#PIECHARTS 
pie(table(age)) 
pie(table(gender)) 
pie(table(approv_in_adv)) 
pie(table(loan_type)) 
pie(table(loan_purpose)) 
pie(table(open_credit)) 
pie(table(business_or_commercial)) 
pie(table(neg_ammortization)) 
pie(table(interest_only)) 
pie(table(lump_sum_payment)) 
pie(table(occupancy_type)) 
pie(table(secured_by))

#BOXPLOTS
boxplot(LTV[age=="25-34"],LTV[age=="35-44"], 
        col =c("blue","pink"),
        names=c("25-34","35-44"), horizontal = TRUE)

#BARPLOTS
hist_data<-function(x,nbins,relfreq=FALSE){
  bin_data <- cut(x,nbins)
  hist_data <- table(bin_data)
  if (relfreq) hist_data <- hist_data/length(x)
  hist_data
}
barplot(hist_data(interest_rate_spread,8,relfreq = TRUE))
barplot(hist_data(rate_of_interest,8,relfreq = TRUE))
barplot(hist_data(term,8,relfreq = TRUE))



mean(loan_default[business_or_commercial=="nob/c",Male]) 

var(income) 
var(loan_amount) 
var(property_value) 
var(LTV)  

sd(income) 
sd(loan_amount) 
sd(property_value) 
sd(LTV)
