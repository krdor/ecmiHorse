library(ggplot2)
library(patchwork)
library(data.table)

getmode <- function(v) {
   uniqv <- unique(v)
   uniqv[which.max(tabulate(match(v, uniqv)))]
}

data <- data.frame(read.csv("game_data.csv", header = TRUE,quote=""))
colnames(data) <- c('User', 'Side', 'Choise', 'Speed_set', 'Won', 'Gender')
mode <- aggregate(data$Choise, by = data[c('Speed_set', 'Side', 'Won')] , FUN = getmode)
colnames(mode)[4]<- 'Frequent Choice'
mode
White <- subset(mode,mode$Side == "W")
Black <- subset(mode,mode$Side == "B")
White
Black
label_y_w <- cumsum(White$`Frequent Choice`) - 0.5 * White$`Frequent Choice`
label_y_w <- cumsum(Black$`Frequent Choice`) - 0.5 * Black$`Frequent Choice`
W <- ggplot(White,                         # Draw barplot with grouping & stacking
       aes(x = Speed_set,
           y = `Frequent Choice`,
           fill = Won)) +
  geom_bar(stat = "identity",
           position = "stack") + labs(title="Most frequent choice playing as White",
        x ="Game Number", y = "Value")+ scale_y_continuous(breaks = seq(from = 0 , to = max(White$`Frequent Choice`)*2, by = 3))+
  geom_text(aes(label = `Frequent Choice`), vjust = 1.5, colour = "white")

B <- ggplot(Black,                         # Draw barplot with grouping & stacking
       aes(x = Speed_set,
           y = `Frequent Choice`,
           fill = Won)) +
  geom_bar(stat = "identity",
           position = "stack") + labs(title="Most frequent choice playing as Black",
        x ="Game Number",
        y = "Value") +
  scale_y_continuous(breaks = seq(from = 0 ,
                                  to = max(Black$`Frequent Choice`), by = 2)) +
  geom_text(aes(label = `Frequent Choice`), vjust = 1.5, colour = "white")

B+W
#
# w_pros_set <- c()
# b_pros_set <- c()
# for (i in 1:5){
#    currW <- subset.data.frame(White, Speed_set == i)
#    currB <- subset.data.frame(Black, Speed_set == i)
#
#
#    b_perb <- nrow(currB$Won == 1)/nrow(currB)
#    w_perb <- nrow(currW$Won == 1)/nrow(currW)
#    b_pros_set <- c(b_pros_set,b_perb)
#    w_pros_set <- c(w_pros_set, w_perb)
#
#    rm(currB)
#    rm(currW)
#
# }
#
#
# w_pros_set
# b_pros_set
# races <- 1:5
# plot(w_pros_set, type = 'l')
# plot(b_pros_set, type = 'l')
# #
# #
# #
# races <- unique(White$Speed_set)
#
# plot(w_pers)

data

White <- data[data$Side=="W",]
Black <- data[data$Side=="B",]
White
Black
b_won_set<- c()
w_won_set<- c()

b_game_set<- c()
w_game_set<- c()

for (i in 1:5){
   wwon <- nrow(White[White$Won==1&White$Speed_set==i,])
   bwon <- nrow(Black[Black$Won==1&Black$Speed_set==i,])
   w_won_set <- c(w_won_set,wwon)
   b_won_set <- c(b_won_set,bwon)
   wgame <- nrow(White[White$Speed_set==i,])
   bgame <- nrow(Black[Black$Speed_set==i,])
   w_game_set <- c(w_game_set,wgame)
   b_game_set <- c(b_game_set,bgame)

}


perc_B <- round(100*b_won_set/b_game_set,1)
perc_W <- round(100*w_won_set/w_game_set,1)


# perB <- table(cut(perc_B,breaks = perc_B, labels = PB))
# perW <- table(cut(perc_W,breaks = perc_W, labels = PW))

PB <- barplot(perc_B, main = "Percentage of winning for Black",col = "black", names = 1:5, xlab = "Speed set", ylab = "%")
text(x = PB, y = perc_B-3.5, labels = perc_B, col="white")

PW <- barplot(perc_W, main = "Percentage of winning for White",col = "white", names = 1:5, xlab = "Speed set", ylab = "%")
text(x = PW, y = perc_W-3.5, labels = perc_W, col = "black")


games_data <- data.frame(w_game_set,w_won_set,b_game_set,b_won_set)
colnames(games_data)<- c("Games(W)", "Won(W)","Games(B)","Won(B)")
games_data

Female <- data[data$Gender == "F",]
Male <- data[data$Gender == "M",]
# Female
# Male
#
# # perc <- c(nrow(Female[Female$Won == 1])/nrow(Female), nrow(Male[Male$Won == 1])/nrow(Male))
# #
# nrow(Female)
# nrow(Male)

# Winner


library(plotrix)

pieM <- c(nrow(Female[Female$Won == 1,]),nrow(Female[Female$Won == 0,]), nrow(Male[Male$Won == 1,]),nrow(Male[Male$Won == 0,]) )
Lables <- c("Female winners","Female loses", "Male wins", "Male loses")
pieDF <- data.frame(pieM,Lables)

# colors <- c("purple","blue","yellow", "green")
# pie3D(pieM, labels = pieM, explode=0.1, main="Results based on gender", col)
# legend(.9, .1, c("DH","UT","AM"), fill = colors)