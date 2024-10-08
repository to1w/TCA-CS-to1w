# 📌 HW Week4 - GET 요청하기

## 1. 제목

Requests 모듈을 활용하여 GET 요청하기

## 2. 이름

> 김가영 (Sophia)


## 3. 제출일

> 24.09.24 (화) 


## 4. 과제 목표

> GET 요청하는 것에 좀 더 익숙해지기 위한 것이라 생각합니다.

## 5. 코드 실행 결과

> 실행한 코드 :
import requests

response = requests.get("https://chatgpt.com/")

print("Status Code:", response.status_code)
print("Response Body:", response.text)

실행한 코드의 결과 :
Status Code: 403
Response Body: <html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style global>body{font-family:Arial,Helvetica,sans-serif}.container{align-items:center;display:flex;flex-direction:column;gap:2rem;height:100%;justify-content:center;width:100%}@keyframes enlarge-appear{0%{opacity:0;transform:scale(75%) rotate(-90deg)}to{opacity:1;transform:scale(100%) rotate(0deg)}}.logo{color:#8e8ea0}.scale-appear{animation:enlarge-appear .4s ease-out}@media (min-width:768px){.scale-appear{height:48px;width:48px}}.data:empty{display:none}.data{border-radius:5px;color:#8e8ea0;text-align:center}@media (prefers-color-scheme:dark){body{background-color:#343541}.logo{color:#acacbe}}</style>
  <meta http-equiv="refresh" content="390">
</head>
  <body>
    <div class="container">
      <div class="logo">
        <svg
          width="41"
          height="41"
          viewBox="0 0 41 41"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          strokeWidth="2"
          class="scale-appear"
        >
          <path
            d="M37.5324 16.8707C37.9808 15.5241 38.1363 14.0974 37.9886 12.6859C37.8409 11.2744 37.3934 9.91076 36.676 8.68622C35.6126 6.83404 33.9882 5.3676 32.0373 4.4985C30.0864 3.62941 27.9098 3.40259 25.8215 3.85078C24.8796 2.7893 23.7219 1.94125 22.4257 1.36341C21.1295 0.785575 19.7249 0.491269 18.3058 0.500197C16.1708 0.495044 14.0893 1.16803 12.3614 2.42214C10.6335 3.67624 9.34853 5.44666 8.6917 7.47815C7.30085 7.76286 5.98686 8.3414 4.8377 9.17505C3.68854 10.0087 2.73073 11.0782 2.02839 12.312C0.956464 14.1591 0.498905 16.2988 0.721698 18.4228C0.944492 20.5467 1.83612 22.5449 3.268 24.1293C2.81966 25.4759 2.66413 26.9026 2.81182 28.3141C2.95951 29.7256 3.40701 31.0892 4.12437 32.3138C5.18791 34.1659 6.8123 35.6322 8.76321 36.5013C10.7141 37.3704 12.8907 37.5973 14.9789 37.1492C15.9208 38.2107 17.0786 39.0587 18.3747 39.6366C19.6709 40.2144 21.0755 40.5087 22.4946 40.4998C24.6307 40.5054 26.7133 39.8321 28.4418 38.5772C30.1704 37.3223 31.4556 35.5506 32.1119 33.5179C33.5027 33.2332 34.8167 32.6547 35.9659 31.821C37.115 30.9874 38.0728 29.9178 38.7752 28.684C39.8458 26.8371 40.3023 24.6979 40.0789 22.5748C39.8556 20.4517 38.9639 18.4544 37.5324 16.8707ZM22.4978 37.8849C20.7443 37.8874 19.0459 37.2733 17.6994 36.1501C17.7601 36.117 17.8666 36.0586 17.936 36.0161L25.9004 31.4156C26.1003 31.3019 26.2663 31.137 26.3813 30.9378C26.4964 30.7386 26.5563 30.5124 26.5549 30.2825V19.0542L29.9213 20.998C29.9389 21.0068 29.9541 21.0198 29.9656 21.0359C29.977 21.052 29.9842 21.0707 29.9867 21.0902V30.3889C29.9842 32.375 29.1946 34.2791 27.7909 35.6841C26.3872 37.0892 24.4838 37.8806 22.4978 37.8849ZM6.39227 31.0064C5.51397 29.4888 5.19742 27.7107 5.49804 25.9832C5.55718 26.0187 5.66048 26.0818 5.73461 26.1244L13.699 30.7248C13.8975 30.8408 14.1233 30.902 14.3532 30.902C14.583 30.902 14.8088 30.8408 15.0073 30.7248L24.731 25.1103V28.9979C24.7321 29.0177 24.7283 29.0376 24.7199 29.0556C24.7115 29.0736 24.6988 29.0893 24.6829 29.1012L16.6317 33.7497C14.9096 34.7416 12.8643 35.0097 10.9447 34.4954C9.02506 33.9811 7.38785 32.7263 6.39227 31.0064ZM4.29707 13.6194C5.17156 12.0998 6.55279 10.9364 8.19885 10.3327C8.19885 10.4013 8.19491 10.5228 8.19491 10.6071V19.808C8.19351 20.0378 8.25334 20.2638 8.36823 20.4629C8.48312 20.6619 8.64893 20.8267 8.84863 20.9404L18.5723 26.5542L15.206 28.4979C15.1894 28.5089 15.1703 28.5155 15.1505 28.5173C15.1307 28.5191 15.1107 28.516 15.0924 28.5082L7.04046 23.8557C5.32135 22.8601 4.06716 21.2235 3.55289 19.3046C3.03862 17.3858 3.30624 15.3413 4.29707 13.6194ZM31.955 20.0556L22.2312 14.4411L25.5976 12.4981C25.6142 12.4872 25.6333 12.4805 25.6531 12.4787C25.6729 12.4769 25.6928 12.4801 25.7111 12.4879L33.7631 17.1364C34.9967 17.849 36.0017 18.8982 36.6606 20.1613C37.3194 21.4244 37.6047 22.849 37.4832 24.2684C37.3617 25.6878 36.8382 27.0432 35.9743 28.1759C35.1103 29.3086 33.9415 30.1717 32.6047 30.6641C32.6047 30.5947 32.6047 30.4733 32.6047 30.3889V21.188C32.6066 20.9586 32.5474 20.7328 32.4332 20.5338C32.319 20.3348 32.154 20.1698 31.955 20.0556ZM35.3055 15.0128C35.2464 14.9765 35.1431 14.9142 35.069 14.8717L27.1045 10.2712C26.906 10.1554 26.6803 10.0943 26.4504 10.0943C26.2206 10.0943 25.9948 10.1554 25.7963 10.2712L16.0726 15.8858V11.9982C16.0715 11.9783 16.0753 11.9585 16.0837 11.9405C16.0921 11.9225 16.1048 11.9068 16.1207 11.8949L24.1719 7.25025C25.4053 6.53903 26.8158 6.19376 28.2383 6.25482C29.6608 6.31589 31.0364 6.78077 32.2044 7.59508C33.3723 8.40939 34.2842 9.53945 34.8334 10.8531C35.3826 12.1667 35.5464 13.6095 35.3055 15.0128ZM14.2424 21.9419L10.8752 19.9981C10.8576 19.9893 10.8423 19.9763 10.8309 19.9602C10.8195 19.9441 10.8122 19.9254 10.8098 19.9058V10.6071C10.8107 9.18295 11.2173 7.78848 11.9819 6.58696C12.7466 5.38544 13.8377 4.42659 15.1275 3.82264C16.4173 3.21869 17.8524 2.99464 19.2649 3.1767C20.6775 3.35876 22.0089 3.93941 23.1034 4.85067C23.0427 4.88379 22.937 4.94215 22.8668 4.98473L14.9024 9.58517C14.7025 9.69878 14.5366 9.86356 14.4215 10.0626C14.3065 10.2616 14.2466 10.4877 14.2479 10.7175L14.2424 21.9419ZM16.071 17.9991L20.4018 15.4978L24.7325 17.9975V22.9985L20.4018 25.4983L16.071 22.9985V17.9991Z"
            fill="currentColor"
          />
        </svg>
      </div>
      <div class="data"><form id="challenge-form" class="challenge-form"><div id="cf-please-wait"><div id="spinner"><div id="cf-bubbles"><div class="bubbles"></div><div class="bubbles"></div><div class="bubbles"></div></div></div><p id="cf-spinner-please-wait"></p><p id="cf-spinner-redirecting" style="display:none"></p></div><noscript id="cf-captcha-bookmark" class="cf-captcha-info"><h1 style="color:#bd2426;">Please turn JavaScript on and reload the page.</h1></noscript><div id="no-cookie-warning" class="cookie-warning" style="display:none"><p style="color:#bd2426;">Please enable Cookies and reload the page.</p></div></form><script>(function(){window._cf_chl_opt={cvId: '3',cZone: "chatgpt.com",cType: 'managed',cNounce: '36987',cRay: '8c83b43b7e88aa80',cHash: '41c769bacc31f29',cUPMDTk: "\/?__cf_chl_tk=FTqw8cfSLTIJAfqmE8FMPvi6stDqayhp2SP425xWUMY-1727190655-0.0.1.1-4372",cFPWv: 'g',cTTimeMs: '1000',cMTimeMs: '390000',cTplV: 1,cTplB: 'cf',cK: "",fa: "\/?__cf_chl_f_tk=FTqw8cfSLTIJAfqmE8FMPvi6stDqayhp2SP425xWUMY-1727190655-0.0.1.1-4372",md: "XK7oN1VJ1vpyGMA4g_fLa5_uTM2bT01iHqJUGbbcV0k-1727190655-1.1.1.1-_oSOD23eFVFFqu6AjGQg266hcTEs3ozPsUFFy2l8wNwWg39OgqGnqndfUn1FuBvqCTorwGDGwPa48qikSCtcbmfIHETBjD3yxscmWepTBS4MIRreIg.IaSoYCwtEOUevtsZRYPJ8Y3NFWeFVvvzGwWkyiSlg3eZl3eM7U.IgRqLnO5f_om17fOXI34k1sfCBLE7bCiie7Tagv5SfsjD79AmIObnXnDczBqtrREK0o8Zu9yqgX.ds3apEYCpRdRH5ps7CyLYcQVwd.bgfp0fJZVogSTf6OPKHlv0oI89Lg8mZPKpLskcCObS9IrGmACnzeAJIp76d706uDOXpstchFz1jeEORBpZNydfpHCd.w6eUhnMEoCKomrxNARkHR40fPtxj3iTRicyAnIM1WxuKU0GFldH8NK6RzHKdErx5TClXomEy3zG0tzrPb57pKeTVM_A4627CIMdZYzcjwLEZ3duzugXonhv1W8SOFlEioFbK0ikQEGl4c2X6L3qsRPsB5ieDc4e8OEnYdJvZvrHbSseZs59jBP65o78d1YxpVyrBTq3YrMziBp84FUw8sh_CtF2.WwnSveqA4l1pTDu587q2PVY2.jAmQtM8XxBUFq.fBAVe1HCkC3UgCoAsibiioHz1qugSokqfD7EhDVquNJh8n1rhiQcmKdWmpQOzLThhn.0mk.nttLT_HxDLK2QwmrNxdgS1VjclGYrhnxU4ebFP5jsmdvx_FcCnNkzvbAzziBQwMdhfl_HdNcVyJXegihusyFNY9RzwywOqZmYW07Di6_2waZ5GNgiPOV1gmystLFGVSJrGkkfUL6iiTuZcK1SK1PpiPgcV_.zlnXBOulF2ccdTjKi81jcQB5kb6Qih1fegFehD2FBo97zwgq2o3LCJzj1feIWt44mN9.uxsjNGO6o4r3UUa0jcbOf9UIA9zohXJQCIP4h.JZbSd.EAijoaNQzCGDExYva63x9aj2SMd_VYyQsTQ9_vhwWc7v3fqsgWqh7DA0Im5oKEXP01iUAJlDXg5NeXrr_RunJegDAqkvbhNQf4euwIsorVnoxo6Yqs.BpG0bxmPXpiJ2.thHIcpxJO5cyzGIomQSyK8iitGfuTxgzNEPvRo7x0vUyEOfEv_RcQRvzVtGGwGHEusSgDuIhNA76zBaPItCCqQ50YMXLqPRG4P_rIcDt99R0uXjOd45DSa4Ajek5i_2SRAmjBlyNIpTFsTkGsAqqV1SRQrjlyA96bH35W26ReMCI7_QSMUrRnPRTrZKGGLRFpb_wfrmL_b._9fD9HgaVqO4LLk5Mv7h9uJSc0qWOoU2XpBfXUKT6hM3fe1gC284O3OPC1o_XCR._oRfLbvbS32wrrdR9D1U5Ky7WwI7lQ6J0YdXtTFlYOaw3FquHxudJ1cGYMnerdakjMq1ObHjXMcTRdkNZHmy3yNDQdymHhASCReCiE5HQzzNxZzK3qrQaOeu7W1AQKyjcXb.hIFXJM0P.nvHW.w1M05KdRMRpGZAFWpWRKEYb1UbErvNOULEWfKvNhUxrRj3ter0ZjU0iuhCxMo9tQgAPqlDiZXnSsZn_q3oxr8KH4ZmCpNUPu_fcyqWPIZN5WOpw1jh8z4G0vYOUIoqRqTRLBlLy_W_SPs61c8Qi02HHXa0D0vCPstX7i28Mivnd5MClNtSgQWA1A4wR9HFsWHzutLKgRcVHtLY2cIqtpMxWvQoMCFnkcecPc9T_AqKSZ_BcCYyxyudfCLX5DJKzLYVwS6z9U55aiWxpmTflyza0W8nm6wBDwtaodLgq8FvR7ryoB4njwtuQkipQWm_ooQC10p8EOYFeSFOZmY9LfZ4Cb4sgkILf4LZYJpsu9aoLJ03ObPdta0DmaYS2XPM8Jyg2XImtV5YtTRZXCgHPGrcHQSXnmyluh2W27BdIFZX0v4Vg_r9SpcXYf3dgR7vq3ZP0J9WVC0hmtSUtc3uHIygsa2tVbKKgnIYxZxRfLO9PKwq5Zf8mWquh0.OuBS13bspYSVyfrtkgGDMGDIs5Zp900NgwxBbCAfnkfbxVn5kcj6cYWntYkMuB3WQ",mdrd: "Zy65nzupBG5KRDoSjZtZWUQZUu2cw0aoCkw1SzZ35Qo-1727190655-1.1.1.1-GGi.mi3f3U0QFWvcW6CFhI2NrxsHbxiYJaobUkEHol6.ClI_065Rj4rzaK7B2zHvzKmF8inZlI_qaqkjWM0ywCKhkMN2tX8GJtp_DLCalankN3YW.ekYOn4zNHBndNfgSGRMKpmLNdug3CHqSCy7r.5g3OlAvS7LESA30NM6m0MAZ7j_UNuJ1yCIuxAQTg2eU9U_4QdpqTPAkw.RWBn_pXTQ50HGpDvX2qYss1zft7kbZnpk_RLetPOz3D8YlUsKUzjqZczhagddBn.KB7rr62PXn3ob9gw6ggSjahAEZeVElYRY_2iZCpROLh1DuF8M2vd6d1p3wJ.Y7hwppGs1LJ.B.2WtPNnMTDoKyqFcsJ3wtp7OkquJOqPAdq_AieAcn3AosU5DskORLVTgRIWB8EHW.RO2yAK1R_XgbnH96qFfSScnG6K9VpomdWttbh7roEbBJfINHi.NhN9jAkyhmmOL7F4QehxQCRLuasqQhRpWIUNALt.EiF9elOFdqj9hVAExt5GZq4fxpBMWZuLAoJroZiFllBwUIEcsA6qh2nIUIfBSb5Umxey0T5XgmUg1kZJCOdFLPFZTqa_0Hhr1XBjthuUhV0z8cBoj42IgKCVBTuOMHbNkRKtk.ZKbH3P_arCbeKFqVPhWRl755GwO.62jv0bySvevERCv43TDKJWLLF9Hove0ZRm.yTcseMqLTLNXKVNlBS97sEwh0fUwb0wqCoH3JR8gfm53hw7XfsSY0j0AqkT.Vg7kMZjPWaWJaWGxksYX.TrOwojVIjGsuQ.20od4Vvn19EiOpZe75p.UNGoDH4oE31SZXV8Kya7FV14IdP1ai_ThnWDEpix6fAWch7ERNMxVITATTHJSgPO1SbjLCCjR1AjDOO.IQK6Cj0deNeD8PtTJbl1AT1VI_LZal5Uh8OkuZtEFSjFq3l5fysQTRpGESYp8x.4T4tmtfXmI.YF.3MIEi0XTLwdL2B3WzjeB8r5MwvGxCxWt1ZYxPQ4Oo3hagwdHJuT9ZD3qv54AKimitbhKT2rMHWGuwuFtsV5dWlJ3xTdIv5PvMfnCZ2jTXQMO503UiNvdQSkNARIE2vj.pRWFz8y2DqFeMNzV.7EWS7nmjjmRaPabhpz8Sr47J8nb_idiv9Q9k3mtMz2HHWHEVJSwhNDX1WQFus87IOJkE7Ai8bsLn.mEGYG.zi2MRwvS83pyhjEH7TaiS_Hx7UvZLGaVVnh2nb.ExmoGqSIdrL6Dg0oZLKpUCIBUm28L7UlhPuAeuXthc38T6eCzp0NYz.kgl_lBzfb0RNfs57vNhcIO2ApVTWrIOg1rMCv8egHJJQpvE5ARECGD.qm0VOekJwYX8XtnH4wrwHrNlD4T1LI4A2u_XPhve0iwk3mN2slQk_XC5LGkL9OLheiyrW7ECcJuUtV8jgxwpZth5mzqJzlohhekpi5CiDN0WtLlSlq3JdCa7jzM7fy.BM27em_Mxodk1ot77Sq_Z8OUVYVFxfrnORxSF1v3pbxidGH8isfJHJ1dy3BHgcnxbe80dBcihSrvoc9RAfYlAoIGgR8UDpdYwtzuwFrnjyfsmFCxfUnaXLTGg6Li4c7mp6w3H842du6SHRYmDU3X1o1TlmSYRxW3vaFj8YAugoxzb6uMvYIZTRx3yEr9EgjeTl_eUbymYWMzFtJOwmJcjL1Jmln_fZWa7xOGQoWGzFgEPOZToZgVoxUE2k9dc3ksecwKns0mH_uzIbwUNBGkj_YKtCJYNl0RKkA7NCo20cgolQXNVGZfsjh7kWVDpO2jjiNtQaBoHf10soSQBIwQJG5I_wEUHg1IANAVV2N8UCbWSsxZADC45HnAxobQCog61tXyUCvcDdsACmnPT4i_bJja64BZza790NOrRC1a2Y5XqWVWaw2xTTd1KGGuwGfqMWpon4XCkAJg0qO7dNnIzbpYti09CBvGzSCABFs2GeJ9yEf2hwashHDisXeJVTHJVYFbpSAllZHiV.gu2tWJ_HJlDvK88XyIW8kcbu6VmIaskgOHA7fnue3ampGq4qaFII_KQnVQDp9.Lajixq6Lu8wAS.L9e.7z8_wH6Ur_Y67.dBQzdb6tHdDjuuxv4gMeM.govNlwPgAvULie_8mBXM4grXLq3Fh8DRUe0_c_fiF2mrfZxXvAzBX___yj.yK1",cRq: {ru: 'aHR0cHM6Ly9jaGF0Z3B0LmNvbS9jaGF0L2Zyb250ZW5kLw==',ra: 'cHl0aG9uLXJlcXVlc3RzLzIuMzIuMw==',d: 'WMFLinKRtZnqjoKYMRObwkbC/SW8Hsv2PFOcRv/sFJC3miFQjhI9PGDRbkmnOPwI7hJeYGf2gb3y7nZWwWMle13Pr04H9JMkLlC/v0bKbv+fBMgMnb4HpKTk0Hu1gxHUCr5bfSMoqQnlbPYHLqupel+PZHeWIp1XGJoIWtJ+pWBXcenX7z0rKKfJlw/lKLNI3cHvoRRH3HTt84LeIkkE65ZVLFreY/CTyHrcCheGrAtFGV/K5S2G+GLiyljRT55Ks0U5A6DpSw+VQqoKp9/7MWQSeOAvdod62ep6nW6W5nG+5XjpaQrykPmWWQDzQeS0RJgKih9AXXyeH+UJbDnw0l/aG25brnB5Nw/yyjpVKi23vH75ViCpLlEr/7CQm17LPFNLnWwnUC7sIlA65VwphwryYGsSgmBj6jOkk4TH5lU6EY2F0y/ijuW2diXAVjQIu773u7JqVEpKzwA663fceLd3MOr5xIlD0yiHFkn76GvxVjD4e5GnjiP6+h9F5PRM4no7/zWVKbymmPFizfthlsXU0KuFvKpe9x3TV/VpZ2InOGLsRWGlzO+l8Uvsr3qDAO7bMgnjU4pdmJ9XlgsZXw==',t: 'MTcyNzE5MDY1NS4wMDAwMDA=',cT: Math.floor(Date.now() / 1000),m: 'ib2xXr7WswTE8+6Ml4gyLBlubjyNWAvLEm8kEi1FQpg=',i1: 'unudE3L5tqGU8/RqHSmmqg==',i2: 'ybiPv6dFT6EpaT4cChrwjQ==',zh: 'u1+pD0dp6zL09EyY2CU2J1ZnCrNrcwtS64dt+csmLfg=',uh: 'CiATXs0R4tTCmAZrIKJMI0mbciEXZbJB6weC9NLv1LY=',hh: '4Ei0+BgjjiWjpS4hlBuK7QB0OxKFiVSABvUyI0X7FcE=',}};var cpo = document.createElement('script');cpo.src = '/cdn-cgi/challenge-platform/h/g/orchestrate/chl_page/v1?ray=8c83b43b7e88aa80';window._cf_chl_opt.cOgUHash = location.hash === '' && location.href.indexOf('#') !== -1 ? '#' : location.hash;window._cf_chl_opt.cOgUQuery = location.search === '' && location.href.slice(0, location.href.length - window._cf_chl_opt.cOgUHash.length).indexOf('?') !== -1 ? '?' : location.search;if (window.history && window.history.replaceState) {var ogU = location.pathname + window._cf_chl_opt.cOgUQuery + window._cf_chl_opt.cOgUHash;history.replaceState(null, null, "\/?__cf_chl_rt_tk=FTqw8cfSLTIJAfqmE8FMPvi6stDqayhp2SP425xWUMY-1727190655-0.0.1.1-4372" + window._cf_chl_opt.cOgUHash);cpo.onload = function() {history.replaceState(null, null, ogU);}}document.getElementsByTagName('head')[0].appendChild(cpo);}());</script></div>
    </div>
  </body>
</html>

## 6. 문제 해결 과정 및 배운점

> 별다른 문제점은 없었으나 "데이터를 가져온다"라는 것에서 정확히 무슨 데이터를 가져온다는걸까 싶어 지피티를 돌려봤습니다. 주요 개념이라며 상태코드, 응답본문, 그리고
쿼리 파라미터라는 것을 배웠는데 응답본문에서 response.content가 바이트 형태로 데이터를 반환한다기에 정확히 뭘까 싶어 다시 한번 돌려봤습니다. 
바이트는 주로 텍스트나 이진 데이터를 다룰 때 사용하며, 문자열 hello를 바이트로 변환하면 각 글자가 특정 숫자로 변환되어 바이트 객체로 만들어지며 컴퓨터가 더 
이해하기 쉬운 형태로 변환되는 것이라 했습니다. 쿼리 파라미터에서 사용되는 params 또한 어떻게 쓰이는 건지 알고싶어 물어봤더니 데이터를 요청할때 전달하는 특정
조건이라 설명했습니다. 형용사랑 비슷하다고 생각되어 이해하는데에는 어려움이 없었습니다. 또한, 위 코드를 실행시켰을때 뜨는 코드 403이 무엇인지 궁금하여 지피티한테
물어보지 403은 리소스는 서버에 있으나 해당 리소스에 접근 권한이 없을 경우에 나타나는 것이라 했습니다. 과제를 하면서 여러 다양한 것을 배운 거 같아 재밌게할 수 
있었어요.