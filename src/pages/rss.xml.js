import rss from "@astrojs/rss";
import { SITE } from "../config";

let allPosts = import.meta.glob("./posts/*.md", { eager: true });
let posts = Object.values(allPosts);
posts = posts.sort((a, b) => {
  return (
    parseInt(b.url.split("/posts/")[1].split("-")[0]) -
    parseInt(a.url.split("/posts/")[1].split("-")[0])
  );
});

//只保留15，当前太多了
posts.splice(15);

export const get = () =>
  rss({
    title: SITE.title,
    description: SITE.description,
    site: SITE.blogPage,
    customData: `<image><url>${SITE.icon}</url></image>`,
    items: posts.map((item, i) => {
      const url = item.url;
      const { title, date } = item.frontmatter;
      return {
        link: url,
        title: `${(i + 1).toString().padStart(2, "0")}.${title} [${date}]`,
        description: item.compiledContent(),
        pubDate: item.frontmatter.date,
      };
    }),
  });
