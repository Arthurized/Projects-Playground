streak_minutes <- c(14, 16, 15, 13, 17, 15, 16, 14, 18, 15, 13, 16, 15, 14, 17)
new_user_minutes <- c(2, 1, 3, 25, 1, 4, 2, 1, 40, 2, 3, 1, 5, 2, 1)

par(mar = c(5, 9, 2, 2))
boxplot(streak_minutes, new_user_minutes,
        names = c("100+ day streak", "New this week"),
        xlab = "Daily active minutes", horizontal = TRUE, las = 1,
        col = c("lightblue", "salmon"),
        outcol = c("blue", "red"), outpch = 19)

par(mfrow = c(2, 1), mar = c(4, 4, 2, 1))

bins <- seq(0, 45, by = 5)   

hist(streak_minutes, breaks = bins, xlim = c(0, 45), ylim = c(0, 13),
     col = "lightblue", main = "100+ day streak",
     xlab = "Daily active minutes", ylab = "Users")

hist(new_user_minutes, breaks = bins, xlim = c(0, 45), ylim = c(0, 13),
     col = "salmon", main = "New this week",
     xlab = "Daily active minutes", ylab = "Users")

par(mfrow = c(1, 1))   # back to one plot per windo

median(c(streak_minutes, new_user_minutes))
sd(c(streak_minutes, new_user_minutes))