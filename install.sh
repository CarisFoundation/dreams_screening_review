#!/bin/bash
# ...existing code...
# Run the following R script
Rscript -e "
install.packages('tidyverse', repos='http://cran.rstudio.com/');
install.packages('RMySQL', repos='http://cran.rstudio.com/');
install.packages('odbc', repos='http://cran.rstudio.com/');
install.packages('DBI', repos='http://cran.rstudio.com/');
install.packages('viridis', repos='http://cran.rstudio.com/');
install.packages('ggplot2', repos='http://cran.rstudio.com/');
install.packages('ggrepel', repos='http://cran.rstudio.com/');
install.packages('ggiraphExtra', repos='http://cran.rstudio.com/');
install.packages('hrbrthemes', repos='http://cran.rstudio.com/');
install.packages('plotly', repos='http://cran.rstudio.com/');
install.packages('stringr', repos='http://cran.rstudio.com/');
install.packages('RColorBrewer', repos='http://cran.rstudio.com/');
install.packages('tidytext', repos='http://cran.rstudio.com/');
install.packages('dplyr', repos='http://cran.rstudio.com/');
install.packages('purrr', repos='http://cran.rstudio.com/');
install.packages('lubridate', repos='http://cran.rstudio.com/');
install.packages('scales', repos='http://cran.rstudio.com/');
install.packages('extrafont', repos='http://cran.rstudio.com/');
install.packages('forcats', repos='http://cran.rstudio.com/');
install.packages('DT', repos='http://cran.rstudio.com/');
install.packages('data.table', repos='http://cran.rstudio.com/');
install.packages('readxl', repos='http://cran.rstudio.com/');
install.packages('reticulate', repos='http://cran.rstudio.com/');
install.packages('kableExtra', repos='http://cran.rstudio.com/');
install.packages('gt', repos='http://cran.rstudio.com/');
"
# ...existing code...
