# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: PlaylistLog
class SearchEngine:
    def __init__(self, data):
        self.data = data
    
    def search(self, query, fields=None):
        if not fields:
            fields = ['title', 'artist', 'album', 'mood']
        
        results = []
        for item in self.data:
            match_count = 0
            normalized_query = query.lower()
            
            for field in fields:
                if field in item and normalized_query in str(item[field]).lower():
                    match_count += 1
            
            if match_count > 0:
                results.append(item)
        
        return results
