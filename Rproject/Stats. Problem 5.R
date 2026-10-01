working_directory <- rstudioapi::getActiveDocumentContext()$path
setwd(dirname(working_directory))

data <- read.csv("payroll2023.csv")

salary_data <- as.numeric(gsub("[$,]", "", data$Base.Salary))

# --- overall salary distribution (before sorting) ---
hist(
  salary_data,
  main = "Histogram of Salaries",
  xlab = "Salary",
  ylab = "Frequency",
  breaks = 20
)

data$Base.Salary.Num <- salary_data
sorted_data <- data[order(data$Base.Salary.Num, decreasing = TRUE), ]
head(sorted_data[, c("Base.Salary", "Pay.Basis", "Base.Salary.Num")], 10)

# --- salary histograms by pay basis (2x2 grid) ---
groups <- unique(data$Pay.Basis)
colors <- rainbow(length(groups))
names(colors) <- groups

par(mfrow = c(2, 2), mar = c(4, 4, 3, 1), cex.main = 0.9)

for (g in groups) {
  vals <- data$Base.Salary.Num[data$Pay.Basis == g]
  h <- hist(
    vals,
    main = paste("Base Salary:", g),
    xlab = "Base Salary ($)",
    ylab = "Frequency",
    breaks = 20,
    col = colors[g],
    xaxt = "n"                                # draw our own axis below
  )
  ticks <- pretty(h$breaks)
  axis(1, at = ticks, labels = paste0("$", ticks / 1000, "k"))
}

par(mfrow = c(1, 1), mar = c(5, 4, 4, 2), cex.main = 1.2)

# --- employees per department ---
dept_counts <- sort(table(data$Agency.Name), decreasing = TRUE)
top_depts <- head(dept_counts, 15)            # top 15; there are many agencies

par(mar = c(5, 14, 4, 2))                     # widen left margin for long names

barplot(
  rev(top_depts),                             # rev() puts the largest at the top
  horiz = TRUE,
  las = 1,                                    # horizontal axis labels
  main = "Employees per Department (Top 15)",
  xlab = "Number of Employees",
  col = hcl.colors(length(top_depts), "Set 2"),
  cex.names = 0.7                             # shrink labels so they fit
)

par(mar = c(5, 4, 4, 2))

# --- annual salary by department (per Annum employees only) ---
annual <- data[data$Pay.Basis == "per Annum", ]

# keep the 12 departments with the most annual-salary employees
top_annual <- names(head(sort(table(annual$Agency.Name), decreasing = TRUE), 12))
annual_top <- annual[annual$Agency.Name %in% top_annual, ]

# shorten very long names so they fit
annual_top$Dept <- ifelse(nchar(annual_top$Agency.Name) > 30,
                          paste0(substr(annual_top$Agency.Name, 1, 28), "..."),
                          annual_top$Agency.Name)

# order departments by median salary
med <- tapply(annual_top$Base.Salary.Num, annual_top$Dept, median)
annual_top$Dept <- factor(annual_top$Dept, levels = names(sort(med)))

# size the left margin to fit the longest department name
label_cex <- 0.75
left_margin <- max(strwidth(levels(annual_top$Dept), units = "inches", cex = label_cex)) + 0.3
par(mai = c(0.9, left_margin, 0.9, 0.4))

boxplot(
  Base.Salary.Num ~ Dept,
  data = annual_top,
  horizontal = TRUE,
  las = 1,
  cex.axis = label_cex,
  col = adjustcolor("steelblue", alpha.f = 0.6),
  border = "steelblue4",
  outpch = 21,
  outbg = adjustcolor("tomato", alpha.f = 0.5),
  outcol = "tomato3",
  outcex = 0.9,
  main = "Annual Base Salary by Department\n(per Annum only)",
  cex.main = 0.95,
  xlab = "",
  ylab = "",
  xaxt = "n"
)

# dollar-formatted x-axis
ticks <- pretty(range(annual_top$Base.Salary.Num), n = 5)
ticks <- ticks[ticks <= max(annual_top$Base.Salary.Num)]
axis(1, at = ticks, labels = paste0("$", format(ticks / 1000, big.mark = ","), "k"))
mtext("Base Salary", side = 1, line = 3)

par(mar = c(5, 4, 4, 2))   # reset margins
