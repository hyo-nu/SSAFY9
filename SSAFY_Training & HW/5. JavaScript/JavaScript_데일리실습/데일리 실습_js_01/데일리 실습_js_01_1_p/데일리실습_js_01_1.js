console.log("*\n**\n***\n****\n*****");
for (let i = 1; i < 6; i++) {
  for (let j = 1; j <= i; j++) {
    process.stdout.write("*");
  }
  console.log();
}

for (let i = 1; i < 6; i++) {
  console.log("*".repeat(i));
}
star = "";
for (let i = 1; i < 6; i++) {
  console.log((star += "*"));
}
