export const BASE_API = 'http://localhost:8000';

export type ReadNote = {
	id: number;
	title: string;
	description?: string | null;
	importance?: string | null;
	create_at: string;
	updated_at: string;
};

export type CreateNote = {
	title: string;
	description?: string | null;
	importance?: string | null;
};

export async function getNotes(search?: string): Promise<ReadNote[]> {
	const url = new URL(`${BASE_API}/notes/`);

	if (search) {
		url.searchParams.set('search', search);
	}

	const result = await fetch(url);

	if (!result.ok) {
		throw new Error('Failed to fetch notes!');
	}

	const data: { notes: ReadNote[] } = await result.json();

	return data.notes;
}

export async function createNotes(data: CreateNote) {
	const url = new URL(`${BASE_API}/notes/`);

	const response = await fetch(url, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	});

	if (!response.ok) {
		const error = await response.json();
		throw new Error(error.detail);
	}
	return response.json();
}

export async function deleteNotes(id: number) {
	const url = new URL(`${BASE_API}/notes/${id}`);

	const response = await fetch(url, {
		method: 'DELETE'
	});

	if (!response.ok) {
		const error = await response.json();
		throw new Error(error.detail);
	}

	if (response.status === 204) {
		return null;
	}

	return response.json();
}
