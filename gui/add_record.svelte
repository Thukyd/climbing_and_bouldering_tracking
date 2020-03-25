<script>
	// TODO: The default value is still not a good option; a user can choose a value and go back to index 0 and still submit!
			// Workaround?= https://github.com/sveltejs/svelte/issues/711
	// TODO: Further information about the "how did you do it?"
	
	let completion_type = [
		{ id: 0, text: `` },
		{ id: 1, text: `Flash` },
		{ id: 2, text: `On-Sight` },
		{ id: 3, text: `Rotpunkt` },
		{ id: 4, text: `Try` }
	];
	
	let scale_type = [
		{ id: 0, text: `` },
		{ id: 1, text: `4` },
		{ id: 2, text: `5` },
		{ id: 3, text: `5+` },
		{ id: 4, text: `6a` },
		{ id: 5, text: `6a+` },
		{ id: 6, text: `6b` },
		{ id: 7, text: `6b+` },
		{ id: 8, text: `6c` },
		{ id: 9, text: `6c+` },
		{ id: 10, text: `7a` },
		{ id: 11, text: `7a+` },
		{ id: 12, text: `7b` },
		{ id: 13, text: `7b+` },
		{ id: 14, text: `7c` },
		{ id: 15, text: `7c+` },
		{ id: 16, text: `8a` },
		{ id: 17, text: `8a+` },
		{ id: 18, text: `8b` },
		{ id: 19, text: `8b+` },
		{ id: 20, text: `8c` },
		{ id: 21, text: `8c+` },
		{ id: 22, text: `9a` }
	]

	let selected_completion = ' ';
	let selected_scale = ' ';
	let answer_notes = '';
	
		function handleSubmit() {
		alert(
			`Completion | index of ${selected_completion.id} which translates to completion type of (${selected_completion.text})\n` +
			`Scale | index of ${selected_scale.id} which translates to scale of (${selected_scale.text})\n` +
			`Notes | "${answer_notes}"`
		);
	}
	
	// watch components: https://framework7.io/svelte/accordion.html


	

</script>


<h2>Add your route:</h2>

<form on:submit|preventDefault={handleSubmit}>
	<p>
	How did you do it?
	</p>
	<select bind:value={selected_completion} on:change="{() => selected_completion}">
		{#each completion_type as completion}
			<option value={completion}>
				{completion.text}
			</option>
		{/each}
	</select>	
<p>
	What grade did you do?
</p>
	<select bind:value={selected_scale} on:change="{() => selected_scale}">
		{#each scale_type as scale}
			<option value={scale}>
				{scale.text}
			</option>
		{/each}
	</select>
<p>
	Extra notes: 
</p>
<p>
	<input bind:value={answer_notes}>
</p>
	
<p>
	
</p>

	<button disabled={selected_completion == 0 | selected_scale == 0} type=submit>
		Submit
	</button>
</form>

<p>
	TODO: add information about the climbing grades. Text and link to youtube: https://www.youtube.com/watch?v=rHsOg_aAEZQ
	
	https://dewiki.de/Lexikon/Begehungsstil#Rotpunkt
	
	
	On-Sight = "first time in one try; without extra knowledge about route";
	Flash = "first time in one try; with extra knowledge"
	Rotpunkt = "multiple tries"
	try = "no successfull try/tries" => Why: Know your challenges for next time
</p>

<!--- DEBUG --->
<p>selected values {selected_completion ? selected_completion.id : '[waiting...]'} and {selected_scale? selected_scale.id : '[waiting...]'} and extra notes: "{answer_notes}""</p>
	