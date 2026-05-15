suppressMessages(library(tidyverse))
scales <- read_csv("D:/R/research/all_scales_v5_FINAL.csv", show_col_types = FALSE)
cat("N rows:", nrow(scales), "\n")
cat("Has dominant_class3:", "dominant_class3" %in% names(scales), "\n")
cat("Has raw_id_num:", "raw_id_num" %in% names(scales), "\n")
cat("Class/subtype cols:\n")
print(grep("class|cluster|subtype", names(scales), value = TRUE, ignore.case = TRUE))
if ("dominant_class3" %in% names(scales)) {
  cat("dominant_class3 distribution:\n")
  print(table(scales$dominant_class3, useNA = "ifany"))
}
