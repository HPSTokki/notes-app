<script lang="ts">
	import type { CreateNote } from '$lib/apis/notes';
	let { onClose, onSubmit }: { onClose: () => void; onSubmit: (data: CreateNote) => void } =
		$props();

	function handleClose() {
		onClose();
	}
	function handleSubmit(e: SubmitEvent) {
		e.preventDefault();
		const form = new FormData(e.currentTarget as HTMLFormElement);

		const data: CreateNote = {
			title: form.get('title') as string,
			description: form.get('description') as string,
			importance: form.get('importance') as string
		};

		onSubmit(data);
		onClose();
	}
</script>

<form
	action="POST"
	class="flex h-auto w-full flex-col items-center justify-center gap-4 rounded bg-green-900 p-6 shadow-sm"
	onsubmit={handleSubmit}
>
	<div class="w-full text-white">
		<label class="floating-label text-slate-300" for="title"> Title </label>
		<input type="text" name="title" id="title" class="input" placeholder="Enter title..." />
	</div>
	<div class="w-full text-white">
		<label class="floating-label text-slate-300" for="description"> Description </label>
		<input
			type="text"
			name="description"
			id="description"
			class="input"
			placeholder="Enter Description..."
		/>
	</div>
	<div class="w-full text-white">
		<label class="floating-label text-slate-300" for="importance"> Importance </label>
		<select name="importance" id="importance" class="select">
			<option class="select-neutral">Personal</option>
			<option class="select-neutral">Important</option>
			<option class="select-neutral">Work</option>
		</select>
	</div>
	<div>
		<button class="btn border-green-600 bg-green-700 shadow-green-900 btn-primary" type="submit">
			Add Note
		</button>
		<button class="btn btn-secondary" type="button" onclick={handleClose}> Cancel </button>
		<button class="btn btn-error" type="reset">Reset Fields</button>
	</div>
</form>
