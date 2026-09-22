app_a <- c(22, 25, 24, 28, 26, 23, 27, 31, 25, 24,
           29, 26, 61, 23, 27, 25, 30, 24, 68, 26)
app_b <- c(16, 19, 21, 23, 25, 27, 28, 29, 30, 31,
           32, 33, 34, 35, 37, 39, 41, 43, 46, 49)

boxplot(app_a, app_b, names = c("App A", "App B"), col = c("Lightblue", "Orange"), outcol = "red",   outpch = 19, 
        main="Two Apps' Delivery Times", ylab = "minutes")