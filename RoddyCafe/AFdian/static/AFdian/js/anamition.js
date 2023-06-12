i = 0
function update_data() {
   amount = parseFloat(sponsorships[i]['show_amount'])
   //金额动态背景、字体颜色
   if (amount <= 30) $("#rank-pill").css("background-image", bg_blue);
   else if (amount <= 99) $("#rank-pill").css("background-image", bg_purple);
   else if (amount <= 499) $("#rank-pill").css("background-image", bg_gold);
   else $("#rank-pill").css("background-image", bg_colorful);

   if(amount >= 100) amount = parseInt(amount)
   //金额动态字体
   switch (amount.toString().length) {
      case 1:
      case 2: $("#rank-amount").css("font-size", "5rem"); break;
      case 3: $("#rank-amount").css("font-size", "4.5rem"); break;
      case 4: $("#rank-amount").css("font-size", "4.2rem"); break;
      case 5: $("#rank-amount").css("font-size", "4rem"); break;
      default:
         break;
   }

   sponsor_name = sponsorships[i]['user']['name']
   sponsor_name = sponsor_name.replace('爱发电用户', 'AFD')
   //ID动态字体
   not_zh_char_amount = 0
   for (let i = 0; i < sponsor_name.length; i++) {
      if(!sponsor_name[i].match(/[\u4e00-\u9fa5]/)) not_zh_char_amount++
   }
   name_too_long = $(window).width() / 85
   name_too_short = $(window).width() / 107
   name_too_too_short = $(window).width() / 117
   char_exist = not_zh_char_amount + (sponsor_name.length - not_zh_char_amount) * 2
   if(char_exist <= name_too_too_short) $("#rank-ID").css("font-size", "5.3rem");
   else if(char_exist <= name_too_short) $("#rank-ID").css("font-size", "5rem");
   else if(char_exist > name_too_long) $("#rank-ID").css("font-size", "3.4rem");
   else $("#rank-ID").css("font-size", "4.3rem");

   //头像
   avator_url = sponsorships[i]['user']['avatar']

   $("#rank-avator").attr("src", avator_url)
   $("#rank-ID").text(sponsor_name)
   $("#rank-amount").text("￥" + amount)
}
$(document).ready(function () {
   setTimeout(() => { }, 3000);
   update_data()
   setInterval(() => {
      i++;
      if(i >= sponsorships.length) {
         setTimeout(() => {
            window.location.reload();
         }, 3000);
      }
      else update_data();
   }, 3000);
});