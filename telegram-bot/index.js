import "dotenv/config";
import { Telegraf } from "telegraf";
import { message } from "telegraf/filters";

async function fetchProduct() {
  const product = await fetch("https://dummyjson.com/products/1").then((res) =>
    res.json(),
  );

  return {
    id: product.id,
    title: product.title,
    price: product.price,
  };
}

const bot = new Telegraf(process.env.BOT_TOKEN);

bot.start((ctx) => ctx.reply("Welcome to bibek's tele bot world"));

bot.command("goodmorning", (ctx) => ctx.reply("Morning Broooo"));
bot.command("hi", (ctx) => ctx.reply("Hey there"));

bot.on(message("sticker"), (ctx) => ctx.reply("👍"));

bot.command("thumb", (ctx) => {
  ctx.reply("👍");
});

bot.command("prod", async (ctx) => {
  const product = await fetchProduct();

  await ctx.reply(JSON.stringify(product, null, 2));
});

bot.on(message("text"), (ctx) => {
  ctx.reply("I don't understand");
});

bot.launch();
