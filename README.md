# ProductRating

For JD Plus members, after evaluating a product, JD will reward Jing beans, but at least 40 words are needed. Therefore, it is necessary to automate the generation of comments.

This project uses the FlagAI model from Zhiyuan to generate a positive or negative evaluation using the product title in the link.

# Prerequisites:

Download the GLM-large-ch model to "./checkpoints/GLM-large-ch/".

Download the AltDiffusion-m9 model to "./checkpoints/AltDiffusion-m9/".

# Steps:

1. Selenium login to the JD account.

2. Jump to the page to be evaluated.

3. Get the product title.

4. Generate evaluation text and images using FlagAI.

   * 4.1 Generate evaluation text using the GLM-large-ch model.

   * 4.2 Generate images using the AltDiffusion-m9 model.

5. Submit.

6. Enter the next product and repeat step 2.

# Requirements

pip install flagai

# Usage
Double click on run.bat to run.
