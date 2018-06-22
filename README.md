<h1 style="text-align: center;">Welcome to Likert 2.0</h1>
					<br>
					<p> As you may know, this software is intended to aid you in the tedious task of processing all the results from the different polls that you may have to do when you try to design a <b>Private Cloud</b> with support for Infrastructure as a Service (<b>IaaS</b>). It has been designed with productivity in mind, so it might take some time to get used to the workflow, but as soon as you get the hang of it we know you'll find it quite useful.</p>

					<p> It's still a work in progress so it'll probably have some <b>bugs</b> here and there, please, feel free to contact us if you find one, or if you have any sugestionss, or if you think this software is cool :)</p>

					<br>
					<h2 >Architecture</h2>

					<p>The software is divided in three sections:</p>
					<ul>
						<li>Main</li>
						<p> Here you must insert the results of your polls, there are two tables, one for the <b>Objectives</b> and one for the <b>Criterions</b>. After you've finished filling the tables you must press the <b>'Check & Run'</b> button so the software can process all your data, and redirect you automatically to the next tab.</p>

						<br>

						<li>Results</li>
						<p>Your automatically generated results will be shown here, they'll be the product of applying the Likert's Scale to all the data you entered in the previous section. It has two tables, one for the <b>Objectives</b> and one for the <b>Criterions</b>. They'll show you which aspects are the most significant according to the people you questioned.</p>

						<br>

						<li>Summary</li>
						<p> Finally, in this sections we'll show you at a bigger scale in which aspects you should focus the design of your cloud.</p>

					</ul> 

					<br>

					<h2>Usage</h2>
					<p> It's pretty simple to use:</p>
					<ul>
						<li>Click in <b>'New'</b> to add a new element</li>
						<li>Fill in the data</li>
						<li>Click <b>'Check & Run'...</b></li>
						<li>And that's all! Your results are ready!</li>
					</ul>

					<p> As we said before, it has been designed with productivity in mind (at least, <b>our</b> idea of productivity). So there are a few things you may want to know...</p>
					<ul>
					<li>	
					<p> In the <b>Main</b> tab, when you're adding a new element, the software brings up a dialog to ask for your data. After you click the <b>'New'</b> button the dialog won't close until you hit the <b>'Close'</b> button. We made it this way so you don't have to be clicking over and over the same button to open the dialog. We changed the way the <b>Significance</b> values are shown in the tables to make them easier to read and give you more room to view the actual text you typed, below each table is a mapping that pairs each showed number with its respective <b>Significance</b> value (incidentally, these numbers also correspond to the weight of each attribute in te <b>Likert's Scale</b>).</p>
				</li>
				<li>
					<p> You can run the software just by doing these things, but it wouldn't be very smart to be re-typing every time you use it, so if you click the <b>'Save'</b> button all the data you entered will be backed up to disk for further use. If you don't do it often you might loose a fair amount of work, so we recommend you to save frequently.</p>
				</li>
				<li>
					<p> In case you made a typo, or entered the wrong data you can select those items by clicking on the checkboxes (or even on the row itself, whichever is easier for you :), and then press the <b>'Delete'</b> button. It's worth mentioning that these deletions aren't permanent unless you say so, if you think you selected the wrong row, as long as you didn't click the <b>'Save'</b> button again, you're good to go! You just have to go to another tab and go back again to the <b>'Main'</b> tab and the original data will be back up again. By the way, you can only delete data from a table if the last element you selected is from that table, for example: if you have several rows selected from both the <b>Objectives</b> and the <b>Criterion</b> tables, when you press the <b>'Delete'</b> button, the elements that will be deleted will be the ones belonging to the table of the last element clicked, this is half good half bug, but we're really confortable with it so we aren't planning on changing it for the moment, if many people complain about this, we'll begin to work on it in future updates.</p>
				</li>
				<li>
					<p> Last but not least, after you press the <b>'Check & Run'</b> button the software will perform a very basic check to see if all the data you passed was valid (it essentially checks if the amount of users you introduced in each row of the tables is bigger than the total of users interviewed, it's the only logical thing we can do to check the veracity of the data, because we already made sure that you can only fill the important fields with the appropriate data types). If a row doesn't pass this test, it will automatically be deleted and you'll be asked if you wanna continue doing the test or want to re-type the missing rows.</p>
				</li>
				<li>
					<p> In the <b>Results</b> step the results are shown, if you are confortable with them you might want to save them by pressing the <b>'Save'</b> button. By design these values aren't automatically loaded at the start of the program, but in case you don't wanna run the software again and just wanna study your previously obtained results you can do this by clicking the <b>'Reload'</b> button, which will load the latest data you saved.</p>
				</li>
			</ul>
					<h2>Known Bugs</h2>
					<ul>
						<li> After clicking <b>'Check & Run'</b> for the first time it will automatically take you to the next tab, but if you go back and hit the button again, it won't take you automatically, you have to manually click the <b>Results</b> tab. </li>

						<li> When you are adding a new Objective, the software has support to automatically suggest you previously typed <b>Values</b>, but, due to bugs in the <b>Vue-material</b> framework, it is shown behind the dialog and the user can't see it, as long as <b>Vue-material</b> fix this, it will be available.</li>

						<li> Depending on your screen size, when you are adding a new row in the <b>Main</b> tab, if, the <b>Objective</b> or <b>Criterion</b> name is too long, it can hide the <b>Buttons</b>, so try to keep the numbers short. This is a major bug, and we're trying to fix it as soon as we can.</li>

						<li> Sometimes, when you click a row in the <b>Main</b> tab, because you want to delete it, the checkboxes doesn't light up, we're are not sure why this is happening, but it's very likely that it's because of a bug in the <b>Vue-material</b> framework. It's not that big of a deal, because, even it the checkbox isn't lighted up, the row is still selected and you can erase it without a problem.</li>

						<li> When you click <b>'Check & Run'</b> and the software determines that you typed invalid data and you still choose to run, since the data doesn't get saved, if all items with a certain  <b>Value</b> are deleted, it still thinks of the names of the deleted <b>Values</b> as valid, but, since they have no data in them, they show up as 0% in the <b>Summary</b> tab, it's a minor bug since it doesn't affect the results of the test, but it's mildly annoying, because it may lead you to think that the data belonging to that <b>Value</b> is insignificant when the reality is that the data you typed was invalid. This happens too for previously assigned <b>Values</b> from other runs of the software.</li>

						<li> Sometimes, when you are adding a new row and leave a field blank (you don't type anything on it), the values of the tables get shifted to the sides and don't allign with the column's header, this happens because of the responsive nature of <b>Vue-material</b> and there's nothing we can do to fix this. If it bothers you that much, you can fix it by saving the tables and the hitting the <b>'Ctrl'+'F5'</b> keys, which will force a reload of the elements in the screen. Anyway, after you restart the application the tables will be properly alligned.</li>

						<li> In the <b>Results</b> tab, when the results are displayed they aren't displayed in order, you must manually click the <b>'Total' </b> column to sort them (it has an arrow indicating that only those values can be sorted)</li>
					</ul>
 
