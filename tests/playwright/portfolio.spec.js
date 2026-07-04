const { test, expect } = require("@playwright/test");

test.describe("Dia Moni portfolio", () => {
  test("homepage sections, navigation, resume, and styling work", async ({ page }) => {
    await page.goto("/");

    await expect(page).toHaveTitle(/Dia Moni/);
    await expect(page.getByRole("heading", { name: "Dia Moni" })).toBeVisible();
    await expect(page.getByText("AI/ML Enthusiast | Python Developer")).toBeVisible();

    const sections = [
      "About Me",
      "Academic Foundation",
      "Technical stack and working strengths",
      "Featured project work",
      "Community involvement and technical initiative",
      "Competitions and recognition",
      "Continuous learning",
      "Open to collaboration",
    ];

    for (const section of sections) {
      await expect(page.getByText(section, { exact: false }).first()).toBeVisible();
    }

    await page.getByRole("link", { name: "Projects" }).click();
    await expect(page.locator("#projects")).toBeInViewport();

    const resumeResponse = await page.goto("/resume");
    expect(resumeResponse.ok()).toBeTruthy();
    await expect(page.getByText("Dia Moni")).toBeVisible();

    await page.goto("/");
    const background = await page.locator("body").evaluate((node) => getComputedStyle(node).backgroundImage);
    expect(background).toContain("gradient");
  });
});
