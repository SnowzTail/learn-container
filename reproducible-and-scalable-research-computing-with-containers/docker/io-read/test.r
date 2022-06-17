library(dplyr)

args <- commandArgs(trailingOnly = TRUE)

print(args[1])

print(args[2])

data <- read.csv(args[1], stringsAsFactors = F)

data_new <- data %>% filter(GENDER == 'MALE')

if (!dir.exists(args[2])) {

  dir.create(args[2])

}

write.csv(data_new, paste(args[2],'output.csv',sep=''))

print("This is a R test in docker!")
